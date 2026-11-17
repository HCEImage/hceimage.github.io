#!/usr/bin/env python3
"""Validate the static site without network access or third-party dependencies.

Checks local destinations/anchors, heading identity, JSON illustrations/downloads and
privacy-policy mirrors in sibling application repositories. It never publishes content.
"""

import html
import json
import re
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


class Page(HTMLParser):
    """Collect references and readable policy text without executing page content."""

    def __init__(self, source):
        super().__init__(convert_charrefs=True)
        self.ids = set()
        self.duplicates = set()
        self.references = []
        self.downloads = []
        self.h1_count = 0
        self.json_examples = []
        self.policy = []
        self.effective_date = []
        self._effective_date = False
        self._policy_depth = 0
        self._policy_header = False
        self._policy_lead = False
        self._code = None
        self.feed(source)

    def handle_starttag(self, tag, attributes):
        attributes = dict(attributes)
        identifier = attributes.get("id")
        if identifier:
            if identifier in self.ids:
                self.duplicates.add(identifier)
            self.ids.add(identifier)
        self.h1_count += tag == "h1"
        if tag == "header" and "policy-header" in attributes.get("class", "").split():
            self._policy_header = True
        if tag == "p" and self._policy_header and "lead" in attributes.get("class", "").split():
            self._policy_lead = True
        if tag == "p" and "effective-date" in attributes.get("class", "").split():
            self._effective_date = True
        for name in ("href", "src"):
            if attributes.get(name):
                self.references.append(attributes[name])
        if tag == "a" and "download" in attributes and attributes.get("href"):
            self.downloads.append(attributes["href"])
        if tag == "div":
            if self._policy_depth:
                self._policy_depth += 1
            elif "policy-content" in attributes.get("class", "").split():
                self._policy_depth = 1
        if tag == "pre":
            self._code = []

    def handle_endtag(self, tag):
        if tag == "header":
            self._policy_header = False
        if tag == "p":
            self._effective_date = False
        if tag == "p" and self._policy_lead:
            self.policy.append(" ")
            self._policy_lead = False
        if tag == "div" and self._policy_depth:
            self._policy_depth -= 1
        if self._policy_depth and tag in ("p", "h2", "li"):
            self.policy.append(" ")
        if tag == "pre" and self._code is not None:
            value = "".join(self._code).strip()
            if value.startswith("{"):
                self.json_examples.append(json.loads(value))
            self._code = None

    def handle_data(self, data):
        if self._effective_date:
            self.effective_date.append(data)
        if self._policy_depth or self._policy_lead:
            self.policy.append(data)
        if self._code is not None:
            self._code.append(data)


def normalized_text(value):
    return " ".join(html.unescape(value).split())


def markdown_policy(value):
    """Compare body/sections, excluding the separately presented title/effective date."""
    value = "\n".join(value.splitlines()[4:])
    value = re.sub(r"\[([^]]+)\]\([^)]*\)", r"\1", value)
    value = re.sub(r"(?m)^#+\s*", "", value)
    return normalized_text(value.replace("**", "").replace("`", ""))


def markdown_effective_date(value):
    """Read the policy date independently of its Markdown emphasis/presentation."""
    match = re.search(r"(?m)^\*\*Effective date: ([^*]+)\*\*$", value)
    return normalized_text("Effective date: " + match[1]) if match else ""


def has_external_source_name(value):
    """Public copy/downloads must not expose the private source-tool name."""
    return re.search(r"btt|\bbrand\s+test\s+tool\b", value, re.IGNORECASE) is not None


def public_copy_errors(value):
    """Keep public HTML about shipped behavior, without product versions or roadmap status."""
    errors = []
    if has_external_source_name(value):
        errors.append("external source name in public HTML")
    value = html.unescape(value)
    if re.search(
        r"\becr\b|\bcash[\s-]*registers?\b|\bnexo\b|\blocal[\s-]+poi\b|\bpokladn\w*",
        value, re.IGNORECASE,
    ):
        errors.append("unrelated application or cash-register content in public HTML")
    if re.search(r"\b(?:v)?\d+\.\d+\.\d+\b", value, re.IGNORECASE):
        errors.append("application release number in public HTML")
    if re.search(r"\b(?:roadmap|planned features?|in development|coming soon)\b", value, re.IGNORECASE):
        errors.append("roadmap or development status in public HTML")
    return errors


def envelope_signature(document):
    return (
        document.get("format"), document.get("kind"),
        document.get("schemaVersion"), document["payload"].get("schemaVersion"),
    )


PROFILE_ENVELOPE = ("com.hceimage.definition", "card-profile", 1, 3)
TRACE_ENVELOPE = ("com.hceimage.diagnostic", "emv-analysis", 1, 2)

def profile_guidance_errors(payload):
    """Check the public examples' guidance contract, not cryptography or native import validity."""
    errors = []
    scenarios = payload.get("testScenarios", [])
    if not isinstance(scenarios, list) or not scenarios:
        return ["missing Test guidance scenarios"]
    ids = set()
    for scenario in scenarios:
        if not isinstance(scenario, dict):
            errors.append("invalid guidance scenario")
            continue
        identifier = scenario.get("id", "")
        if not isinstance(identifier, str) or not identifier or identifier in ids:
            errors.append("missing or duplicate guidance scenario ID")
        else:
            ids.add(identifier)
        for field in ("name", "transactionType", "amountCondition", "expectedCvm", "expectedOutcome"):
            if not isinstance(scenario.get(field), str) or not scenario[field].strip():
                errors.append(f"{identifier}: missing {field}")
        if scenario.get("amountCondition") != "ANY" and (
            not isinstance(scenario.get("amountNote"), str) or not scenario["amountNote"].strip()
        ):
            errors.append(f"{identifier}: missing amountNote for a bounded amount")
        for field in ("terminalSetup", "knownLimitations"):
            values = scenario.get(field)
            if not isinstance(values, list) or not values or any(
                not isinstance(value, str) or not value.strip() for value in values
            ):
                errors.append(f"{identifier}: invalid {field}")
        pin = scenario.get("testPin")
        note = scenario.get("pinNote", "")
        if scenario.get("expectedCvm") == "ONLINE_PIN":
            if not isinstance(pin, str) or not re.fullmatch(r"[0-9]{4,12}", pin):
                errors.append(f"{identifier}: missing structured test PIN")
            if not isinstance(note, str) or "does not verify" not in note:
                errors.append(f"{identifier}: missing PIN verification boundary")
        if isinstance(pin, str) and pin and isinstance(note, str) and pin in note:
            errors.append(f"{identifier}: PIN repeated in prose")
        if has_external_source_name(json.dumps(scenario, ensure_ascii=False)):
            errors.append(f"{identifier}: external source name in public guidance")
    return errors


PUBLIC_EXAMPLES = {
    "visa-online-pin.hceimage.json": "VISA",
    "mastercard-online-pin.hceimage.json": "MASTERCARD",
    "amex-online-pin.hceimage.json": "AMERICAN_EXPRESS",
    "jcb-online-pin.hceimage.json": "JCB",
}

POLICY_APPS = ("hce-test-tool", "emv-card-analyzer")
GUIDANCE_TARGETS = (
    "/guides/hce-test-tool/#test-flow",
    "/guides/hce-test-tool/#import-profiles",
    "/guides/hce-test-tool/#history-reports",
    "/guides/hce-test-tool/#settings",
    "/guides/emv-card-analyzer/#analysis-flow",
    "/guides/emv-card-analyzer/#history-reports",
    "/guides/emv-card-analyzer/#settings-safety",
    "/guides/hceimage-json/#card-profile",
    "/guides/hceimage-json/#analysis-trace",
)
PUBLIC_ROUTES = frozenset({
    "/",
    "/guides/",
    "/guides/hce-test-tool/",
    "/guides/emv-card-analyzer/",
    "/guides/hceimage-json/",
    "/hce-test-tool/privacy-policy/",
    "/emv-card-analyzer/privacy-policy/",
})


def route_inventory_errors(page_routes, sitemap_routes):
    """Keep published pages and sitemap limited to the supported application routes."""
    errors = []
    if set(page_routes) != PUBLIC_ROUTES or len(page_routes) != len(PUBLIC_ROUTES):
        errors.append("Public HTML routes differ from the supported website inventory")
    if set(sitemap_routes) != PUBLIC_ROUTES or len(sitemap_routes) != len(PUBLIC_ROUTES):
        errors.append("Sitemap must list each supported public route exactly once")
    return errors


def guidance_target_errors(pages_by_route):
    """Preserve every chapter opened by primary-tab guidance and its format references."""
    errors = []
    for reference in GUIDANCE_TARGETS:
        target = urlsplit(reference)
        page = pages_by_route.get(target.path)
        if page is None or target.fragment not in page.ids:
            errors.append(f"Missing in-app guidance destination: {reference}")
    return errors


def example_inventory_errors(brands_by_filename):
    """Keep every supported brand represented exactly once under its stable download name."""
    errors = []
    if set(brands_by_filename) != set(PUBLIC_EXAMPLES):
        errors.append("Expected exactly one public example for each supported brand")
    for filename, brand in brands_by_filename.items():
        if filename not in PUBLIC_EXAMPLES or brand != PUBLIC_EXAMPLES[filename]:
            errors.append(f"{filename}: example brand does not match its download")
    return errors


def example_download_errors(downloads):
    """Check that all stable profile files have exactly one local download action."""
    expected = {
        "/guides/hceimage-json/examples/" + filename for filename in PUBLIC_EXAMPLES
    }
    paths = []
    for download in downloads:
        target = urlsplit(download)
        path = unquote(target.path)
        if target.scheme or target.netloc or not path.startswith("/"):
            return ["Profile download actions must use local, root-relative URLs"]
        paths.append(path)
    if set(paths) != expected or len(paths) != len(expected):
        return ["The JSON guide must link once to each public profile download"]
    return []


def check_site(root):
    root = root.resolve()
    pages = {path.resolve(): Page(path.read_text()) for path in root.rglob("*.html")}
    errors = []
    page_routes = []
    for path in pages:
        relative = path.relative_to(root)
        if relative.as_posix() == "index.html":
            page_routes.append("/")
        elif relative.name == "index.html":
            page_routes.append("/" + relative.parent.as_posix() + "/")
        else:
            page_routes.append("/" + relative.as_posix())
    sitemap = ET.parse(root / "sitemap.xml")
    sitemap_routes = [
        urlsplit(location.text).path
        for location in sitemap.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc")
    ]
    errors.extend(route_inventory_errors(page_routes, sitemap_routes))
    errors.extend(guidance_target_errors(dict(zip(page_routes, pages.values()))))
    references = 0
    for path, page in pages.items():
        relative = path.relative_to(root)
        errors.extend(f"{relative}: {issue}" for issue in public_copy_errors(path.read_text()))
        if page.h1_count != 1:
            errors.append(f"{relative}: expected one H1, found {page.h1_count}")
        if page.duplicates:
            errors.append(f"{relative}: duplicate anchors {sorted(page.duplicates)}")
        for reference in page.references:
            target = urlsplit(reference)
            if target.scheme or target.netloc:
                continue
            references += 1
            destination = (
                root / unquote(target.path).lstrip("/")
                if target.path.startswith("/")
                else path.parent / unquote(target.path)
            )
            if not target.path:
                destination = path
            destination = destination.resolve()
            if not destination.is_relative_to(root):
                errors.append(f"{relative}: reference escapes site: {reference}")
                continue
            if destination.is_dir():
                destination /= "index.html"
            if not destination.is_file():
                errors.append(f"{relative}: missing destination {reference}")
            elif target.fragment and (
                destination not in pages
                or unquote(target.fragment) not in pages[destination].ids
            ):
                errors.append(f"{relative}: missing anchor {reference}")
    profiles = list((root / "guides/hceimage-json/examples").glob("*.hceimage.json"))
    json_guide = pages[root / "guides/hceimage-json/index.html"]
    errors.extend(example_download_errors(json_guide.downloads))
    if [envelope_signature(example) for example in json_guide.json_examples] != [
        PROFILE_ENVELOPE, TRACE_ENVELOPE,
    ]:
        errors.append("The JSON guide must illustrate the supported profile and trace envelopes")
    elif any(key in json_guide.json_examples[-1]["payload"] for key in ("evidence", "payloadVersion")):
        errors.append("The schema 2 trace example must omit evidence and payloadVersion")
    documents = {path.name: json.loads(path.read_text()) for path in profiles}
    errors.extend(example_inventory_errors({
        name: document["payload"].get("brand") for name, document in documents.items()
    }))
    ids = set()
    for path in profiles:
        document = documents[path.name]
        payload = document["payload"]
        if has_external_source_name(json.dumps(document, ensure_ascii=False)):
            errors.append(f"{path.name}: external source name in public download")
        if payload.get("source") != {"format": "CUSTOM"}:
            errors.append(f"{path.name}: public downloads require CUSTOM-only provenance")
        if envelope_signature(document) != PROFILE_ENVELOPE:
            errors.append(f"{path.name}: unexpected profile envelope/schema")
        if payload["id"] in ids:
            errors.append(f"{path.name}: duplicate Profile ID")
        ids.add(payload["id"])
        errors.extend(f"{path.name}: {issue}" for issue in profile_guidance_errors(payload))
    for app in POLICY_APPS:
        try:
            policy_text = (root.parent / app / "play/privacy-policy.md").read_text()
        except OSError:
            errors.append(f"{app}: missing application policy")
            continue
        page = pages.get(root / app / "privacy-policy/index.html")
        if page is None:
            errors.append(f"{app}: missing website policy")
            continue
        expected_date = markdown_effective_date(policy_text)
        if not expected_date or expected_date != normalized_text("".join(page.effective_date)):
            errors.append(f"{app}: website privacy effective date differs from application policy")
        if markdown_policy(policy_text) != normalized_text("".join(page.policy)):
            errors.append(f"{app}: website privacy body differs from application policy")
    return errors, len(pages), references, len(profiles)


if __name__ == "__main__":
    issues, page_count, link_count, profile_count = check_site(Path(__file__).resolve().parents[1])
    if issues:
        raise SystemExit("\n".join(issues))
    print(
        f"PASS: {page_count} HTML pages, {link_count} local references, "
        f"{profile_count} profile envelopes, JSON illustrations and {len(POLICY_APPS)} policy mirrors."
    )
