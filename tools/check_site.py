#!/usr/bin/env python3
"""Validate the static site without network access or third-party dependencies.

Checks local destinations/anchors, heading identity, JSON illustrations/downloads and
privacy-policy mirrors in sibling application repositories. It never publishes content.
"""

import html
import json
import re
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
        self.h1_count = 0
        self.json_examples = []
        self.policy = []
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
        for name in ("href", "src"):
            if attributes.get(name):
                self.references.append(attributes[name])
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


def check_site(root):
    root = root.resolve()
    pages = {path.resolve(): Page(path.read_text()) for path in root.rglob("*.html")}
    errors = []
    references = 0
    for path, page in pages.items():
        relative = path.relative_to(root)
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
    ids = set()
    for path in profiles:
        document = json.loads(path.read_text())
        payload = document["payload"]
        actual = (
            document.get("format"), document.get("kind"),
            document.get("schemaVersion"), payload.get("schemaVersion"),
        )
        if actual != (
            "com.hceimage.definition", "card-profile", 1, 2,
        ):
            errors.append(f"{path.name}: unexpected profile envelope/schema")
        if payload["id"] in ids:
            errors.append(f"{path.name}: duplicate Profile ID")
        ids.add(payload["id"])
    for app in ("hce-test-tool", "emv-card-analyzer", "ecr-test-tool"):
        policy = root.parent / app / "play/privacy-policy.md"
        if not policy.is_file():
            errors.append(f"Missing sibling privacy policy: {policy}")
        else:
            page = pages[root / app / "privacy-policy/index.html"]
            if markdown_policy(policy.read_text()) != normalized_text("".join(page.policy)):
                errors.append(f"{app}: website privacy body differs from application policy")
    return errors, len(pages), references, len(profiles)


if __name__ == "__main__":
    issues, page_count, link_count, profile_count = check_site(Path(__file__).resolve().parents[1])
    if issues:
        raise SystemExit("\n".join(issues))
    print(
        f"PASS: {page_count} HTML pages, {link_count} local references, "
        f"{profile_count} profile envelopes, JSON illustrations and 3 policy mirrors."
    )
