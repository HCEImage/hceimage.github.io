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
        self.section_ids = []
        self.shortcut_targets = []
        self.quick_start_steps = 0
        self.walkthrough_images = []
        self._walkthrough_depth = 0
        self._image_link = None
        self._guide_shortcuts = False
        self._quick_start_list = False
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
        if tag == "a":
            self._image_link = attributes.get("href")
        if tag == "div":
            if self._walkthrough_depth:
                self._walkthrough_depth += 1
            elif "walkthrough-gallery" in attributes.get("class", "").split():
                self._walkthrough_depth = 1
        if tag == "img" and self._walkthrough_depth:
            self.walkthrough_images.append((
                attributes.get("src"), self._image_link, attributes.get("alt", ""),
                attributes.get("width"), attributes.get("height"),
            ))
        identifier = attributes.get("id")
        if identifier:
            if identifier in self.ids:
                self.duplicates.add(identifier)
            self.ids.add(identifier)
        self.h1_count += tag == "h1"
        if tag == "section" and attributes.get("aria-labelledby"):
            self.section_ids.append(attributes["aria-labelledby"])
        if tag == "nav" and attributes.get("aria-label") == "Guide shortcuts":
            self._guide_shortcuts = True
        if tag == "a" and self._guide_shortcuts:
            self.shortcut_targets.append(attributes.get("href"))
        if tag == "ol" and "quick-start-steps" in attributes.get("class", "").split():
            self._quick_start_list = True
        if tag == "li" and self._quick_start_list:
            self.quick_start_steps += 1
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
        if tag == "a":
            self._image_link = None
        if tag == "div" and self._walkthrough_depth:
            self._walkthrough_depth -= 1
        if tag == "nav":
            self._guide_shortcuts = False
        if tag == "ol":
            self._quick_start_list = False
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
# Released runtime sources: HCE 79a26e7 (1.0.0) and Analyzer aaeb5c1 (0.2.0).
# Keep roots used by those binaries even when current app guidance uses chapter fragments.
RELEASED_APPLICATION_TARGETS = frozenset({
    "https://hceimage.github.io/guides/hce-test-tool/",
    "https://hceimage.github.io/guides/hce-test-tool/#history-reports",
    "https://hceimage.github.io/guides/hceimage-json/",
    "https://hceimage.github.io/hce-test-tool/privacy-policy/",
    "https://hceimage.github.io/guides/emv-card-analyzer/",
    "https://hceimage.github.io/guides/hceimage-json/#analysis-trace",
    "https://hceimage.github.io/emv-card-analyzer/privacy-policy/",
})
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

# Existing public fragments are compatibility identifiers, not presentation headings.
PUBLIC_ANCHORS = {
    "/": {"hero-title", "applications", "applications-title"},
    "/guides/": {"application-guides-title", "exchange-formats-title"},
    "/guides/hce-test-tool/": {
        "development-profiles", "before-starting", "test-flow", "inspect-exchange",
        "history-reports", "workspace-lifecycle", "security-data", "simulated-device-cvm",
        "import-profiles", "profile-format-title", "copy-profiles", "settings",
    },
    "/guides/emv-card-analyzer/": {
        "before-starting", "analysis-flow", "contactless-support", "result-states",
        "inspect-data", "diagnostic-findings", "response-timing", "workspace-lifecycle",
        "history-reports", "trace-format-title", "settings-safety", "data-safety",
    },
    "/guides/hceimage-json/": {
        "envelope", "card-profile", "legacy-security", "profile-examples", "analysis-trace", "compatibility",
    },
    "/hce-test-tool/privacy-policy/": {
        "collection", "local-data", "test-security-data", "simulated-verification", "clipboard-logs",
        "reports", "nfc", "children", "hosting", "changes", "contact",
    },
    "/emv-card-analyzer/privacy-policy/": {
        "collection", "local-data", "scope", "copying-diagnostics", "reports", "nfc", "children",
        "hosting", "changes", "contact",
    },
}
APPLICATION_LINK_SOURCES = (
    ("hce-test-tool", "shared/ui/src/commonMain/kotlin/com/hceimage/hcetesttool/ui/ContextualGuidanceSheet.kt"),
    ("hce-test-tool", "shared/ui/src/commonMain/kotlin/com/hceimage/hcetesttool/ui/CardTestGuidance.kt"),
    ("hce-test-tool", "shared/ui/src/commonMain/kotlin/com/hceimage/hcetesttool/ui/PrivacyPolicy.kt"),
    ("emv-card-analyzer", "shared/ui/src/commonMain/kotlin/com/hceimage/emvcardanalyzer/ui/ContextualGuidance.kt"),
    ("emv-card-analyzer", "shared/ui/src/commonMain/kotlin/com/hceimage/emvcardanalyzer/ui/DevelopmentUseNotice.kt"),
)


def public_anchor_errors(pages_by_route):
    """Retain old deep links even when chapters move or their visible titles change."""
    errors = []
    for route, anchors in PUBLIC_ANCHORS.items():
        actual = pages_by_route[route].ids if route in pages_by_route else set()
        errors.extend(f"Missing stable public anchor: {route}#{anchor}" for anchor in sorted(anchors - actual))
    return errors


def application_targets(source):
    """Read direct URLs and the apps' explicit Kotlin chapter-selection tables; never execute source."""
    urls = set(re.findall(r'"(https://hceimage\.github\.io/[^"\s]*)"', source))
    mappings = re.findall(
        r'"(https://hceimage\.github\.io/[^"\s]*#)"\s*\+\s*when\s*\([^)]*\)\s*\{([^}]+)\}',
        source,
    )
    expanded = set()
    for prefix, branches in mappings:
        fragments = re.findall(r'ScreenGuidance\.\w+\s*->\s*"([a-z0-9-]+)"', branches)
        if fragments:
            urls.discard(prefix)
            expanded.update(prefix + fragment for fragment in fragments)
    errors = [f"Unresolved application guidance URL: {url}" for url in sorted(urls) if url.endswith("#")]
    return {url for url in urls if not url.endswith("#")} | expanded, errors


def application_target_errors(urls, pages_by_route):
    """Resolve the destinations actually used by app source against this local website."""
    errors = []
    for url in sorted(urls):
        target = urlsplit(url)
        page = pages_by_route.get(target.path)
        if page is None or (target.fragment and unquote(target.fragment) not in page.ids):
            errors.append(f"Missing application link destination: {url}")
    return errors


def quick_start_errors(pages_by_route):
    """Keep both guides on the same prerequisites, single presentation, result progression."""
    errors = []
    for route, flow, result, settings in (
        ("/guides/hce-test-tool/", "test-flow", "inspect-exchange", "settings"),
        ("/guides/emv-card-analyzer/", "analysis-flow", "result-states", "settings-safety"),
    ):
        page = pages_by_route.get(route)
        if page is None:
            errors.append(f"Missing quick-start guide: {route}")
            continue
        if page.section_ids[:3] != ["before-starting", flow, result]:
            errors.append(f"{route}: quick start and result must precede advanced reference")
        if page.quick_start_steps != 3:
            errors.append(f"{route}: expected three single-presentation quick-start steps")
        if page.shortcut_targets != ["#before-starting", "#" + flow, "#" + result, "#history-reports", "#" + settings]:
            errors.append(f"{route}: primary guide shortcuts differ from the shared navigation contract")
    return errors


WALKTHROUGH_IMAGES = {
    "/guides/hce-test-tool/": (
        "/assets/hce-single-tap-emulator.jpg", "/assets/hce-single-tap-result.jpg",
        "/assets/hce-single-tap-apdu-exchange.jpg", "/assets/hce-single-tap-apdu-response.jpg",
    ),
    "/guides/emv-card-analyzer/": (
        "/assets/emv-single-tap-ready.jpg", "/assets/emv-analysis-summary.jpg",
        "/assets/emv-apdu-exchange.jpg", "/assets/emv-apdu-response.jpg",
    ),
}


def walkthrough_image_errors(pages_by_route):
    """Keep matching, full-size-linked native UI examples in both first-use guides."""
    errors = []
    for route, expected in WALKTHROUGH_IMAGES.items():
        page = pages_by_route.get(route)
        images = page.walkthrough_images if page else []
        if tuple(image[0] for image in images) != expected:
            errors.append(f"Wrong single-presentation screenshot order: {route}")
        for source, link, alternate, width, height in images:
            if source != link or not alternate.strip() or (width, height) != ("1080", "1920"):
                errors.append(f"Screenshot needs a full-size link, alt text and native dimensions: {route} {source}")
    homepage = pages_by_route.get("/")
    if not homepage or "/assets/hce-single-tap-emulator.jpg" not in homepage.references:
        errors.append("Homepage HCE preview must show the Emulator")
    if not homepage or "/assets/emv-single-tap-ready.jpg" not in homepage.references:
        errors.append("Homepage EMV preview must show the prepared Analyzer")
    return errors


def quick_start_profile_errors(payload, guide_source):
    """Bind the first HCE scenario to the actual native Built-in definition, not its display name alone."""
    errors = []
    if payload.get("id") != "mastercard-physical-emv-no-cvm-signature" or (
        payload.get("brand"), payload.get("formFactor")
    ) != ("MASTERCARD", "PHYSICAL"):
        errors.append("HCE quick start requires the selected physical Mastercard baseline")
    if not payload.get("name") or payload["name"] not in html.unescape(guide_source):
        errors.append("HCE quick-start profile name differs from the native catalog")
    if not any(
        isinstance(scenario, dict) and scenario.get("amountCondition") == "BELOW_CVM_LIMIT"
        and scenario.get("expectedCvm") == "NO_CVM"
        for scenario in payload.get("testScenarios", [])
    ):
        errors.append("HCE quick-start profile lacks the documented below-limit No CVM scenario")
    return errors


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
    pages_by_route = dict(zip(page_routes, pages.values()))
    errors.extend(guidance_target_errors(pages_by_route))
    errors.extend(public_anchor_errors(pages_by_route))
    errors.extend(quick_start_errors(pages_by_route))
    errors.extend(walkthrough_image_errors(pages_by_route))
    errors.extend(application_target_errors(RELEASED_APPLICATION_TARGETS, pages_by_route))
    for app, source_path in APPLICATION_LINK_SOURCES:
        try:
            source = (root.parent / app / source_path).read_text()
        except OSError:
            errors.append(f"{app}: missing guidance-link source {source_path}")
            continue
        targets, unresolved = application_targets(source)
        errors.extend(unresolved)
        if not targets:
            errors.append(f"{app}: no website destinations found in {source_path}")
        errors.extend(application_target_errors(targets, pages_by_route))
    try:
        profile = json.loads((
            root.parent / "hce-test-tool/card-images/mastercard/mastercard-physical-emv-no-cvm-signature.hceimage.json"
        ).read_text())["payload"]
        errors.extend(quick_start_profile_errors(profile, (root / "guides/hce-test-tool/index.html").read_text()))
    except (OSError, ValueError, KeyError, TypeError):
        errors.append("HCE quick-start native profile definition is unavailable or invalid")
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
