"""Small parser regressions; run with python3 -m unittest discover -s tools."""

import unittest

from check_site import (
    PUBLIC_EXAMPLES,
    Page,
    example_download_errors,
    example_inventory_errors,
    has_external_source_name,
    markdown_effective_date,
    markdown_policy,
    normalized_text,
    profile_guidance_errors,
)


class SiteParserTest(unittest.TestCase):
    def test_duplicate_anchors_are_not_silently_overwritten(self):
        page = Page('<h1 id="one">Title</h1><h2 id="one">Duplicate</h2>')
        self.assertEqual({"one"}, page.duplicates)
        self.assertEqual(1, page.h1_count)

    def test_references_and_escaped_json_are_preserved(self):
        page = Page(
            '<a href="/guide/#field">Guide</a>'
            '<pre><code>{"name":"&lt;example&gt;"}</code></pre>'
        )
        self.assertEqual(["/guide/#field"], page.references)
        self.assertEqual([{"name": "<example>"}], page.json_examples)

    def test_download_actions_are_distinct_from_view_links(self):
        page = Page('<a href="/example.json" download>Download</a><a href="/example.json">View</a>')
        self.assertEqual(["/example.json"], page.downloads)

    def test_policy_comparison_ignores_presentation_not_words(self):
        page = Page(
            '<nav>Other text</nav><div class="policy-content"><h2>Scope</h2>'
            '<p>Local <strong>only</strong>.</p></div><footer>Footer</footer>'
        )
        markdown = "# Policy\n\n**Effective date: today**\n\n## Scope\n\nLocal **only**.\n"
        self.assertEqual(markdown_policy(markdown), normalized_text("".join(page.policy)))
        self.assertNotEqual(
            markdown_policy(markdown.replace("only", "upload")),
            normalized_text("".join(page.policy)),
        )

    def test_policy_lead_is_included_without_title_or_effective_date(self):
        page = Page(
            '<header class="policy-header"><h1>Policy</h1>'
            '<p class="effective-date">Today</p><p class="lead">Local tool.</p></header>'
            '<div class="policy-content"><h2>Scope</h2><p>No upload.</p></div>'
        )
        self.assertEqual("Local tool. Scope No upload.", normalized_text("".join(page.policy)))


class PublicSourceNameTest(unittest.TestCase):
    def test_external_name_is_rejected_in_copy_paths_and_metadata(self):
        for value in ("BTT", "btt", "BTT_CARD_IMAGE", "archive/Btt/profile.xml", "Brand Test Tool"):
            self.assertTrue(has_external_source_name(value))
        self.assertFalse(has_external_source_name('{"source":{"format":"CUSTOM"}}'))


class PolicyDateTest(unittest.TestCase):
    def test_date_is_separate_and_cannot_be_replaced_by_body_text(self):
        page = Page(
            '<header class="policy-header"><p class="effective-date">Effective date: November 9, 2026</p>'
            '<p class="lead">No automatic upload.</p></header>'
        )
        markdown = "# Policy\n\n**Effective date: November 9, 2026**\n"
        self.assertEqual(markdown_effective_date(markdown), "".join(page.effective_date))
        self.assertNotEqual(markdown_effective_date(markdown.replace("9,", "8,")), "".join(page.effective_date))
        self.assertEqual("", markdown_effective_date("# Missing date"))


class ExampleInventoryTest(unittest.TestCase):
    def test_download_actions_cover_all_stable_files_once(self):
        downloads = ["/guides/hceimage-json/examples/" + name for name in PUBLIC_EXAMPLES]
        self.assertEqual([], example_download_errors(downloads))
        self.assertTrue(example_download_errors(downloads[:-1]))
        self.assertTrue(example_download_errors(downloads + downloads[:1]))
        self.assertTrue(example_download_errors(downloads[:-1] + ["/assets/replacement.json"]))

    def test_external_download_cannot_impersonate_a_local_example(self):
        downloads = ["/guides/hceimage-json/examples/" + name for name in PUBLIC_EXAMPLES]
        self.assertTrue(example_download_errors(downloads[:-1] + ["https://example.com" + downloads[-1]]))

    def test_each_supported_brand_has_its_stable_download(self):
        self.assertEqual([], example_inventory_errors(dict(PUBLIC_EXAMPLES)))

    def test_missing_brand_example_is_rejected(self):
        examples = dict(PUBLIC_EXAMPLES)
        del examples["jcb-online-pin.hceimage.json"]
        self.assertTrue(example_inventory_errors(examples))

    def test_extra_download_cannot_silently_duplicate_a_brand(self):
        examples = dict(PUBLIC_EXAMPLES, extra="JCB")
        self.assertTrue(example_inventory_errors(examples))

    def test_brand_cannot_be_swapped_under_another_download_name(self):
        examples = dict(PUBLIC_EXAMPLES)
        examples["jcb-online-pin.hceimage.json"] = "VISA"
        self.assertTrue(example_inventory_errors(examples))


class ProfileGuidanceTest(unittest.TestCase):
    def scenario(self):
        """One complete public physical-example scenario, independent of native crypto fixtures."""
        return {
            "id": "online-pin", "name": "Online PIN purchase", "transactionType": "PURCHASE",
            "amountCondition": "ABOVE_CVM_LIMIT", "amountNote": "Use a configured test reader.",
            "expectedCvm": "ONLINE_PIN", "expectedOutcome": "ONLINE_AUTHORIZATION",
            "testPin": "1234", "pinNote": "The application does not verify the PIN.",
            "terminalSetup": ["Use an authorized test reader."],
            "knownLimitations": ["Card completion is not host approval."],
        }

    def test_complete_structured_pin_guidance_is_accepted(self):
        self.assertEqual([], profile_guidance_errors({"testScenarios": [self.scenario()]}))

    def test_amount_independent_guidance_does_not_require_a_limit_note(self):
        scenario = self.scenario()
        del scenario["amountNote"]
        self.assertTrue(profile_guidance_errors({"testScenarios": [scenario]}))
        scenario["amountCondition"] = "ANY"
        self.assertEqual([], profile_guidance_errors({"testScenarios": [scenario]}))

    def test_empty_guidance_and_non_object_scenarios_are_rejected(self):
        for value in (None, [], "not scenarios", [None]):
            with self.subTest(value=value):
                self.assertTrue(profile_guidance_errors({"testScenarios": value}))

    def test_missing_or_duplicate_ids_are_rejected(self):
        scenario = self.scenario()
        self.assertTrue(profile_guidance_errors({"testScenarios": [scenario, scenario]}))
        scenario["id"] = ""
        self.assertTrue(profile_guidance_errors({"testScenarios": [scenario]}))

    def test_online_pin_requires_digits_and_verification_boundary(self):
        for field, value in (("testPin", None), ("testPin", "１２３４"), ("pinNote", "Verified by app.")):
            scenario = self.scenario()
            scenario[field] = value
            self.assertTrue(profile_guidance_errors({"testScenarios": [scenario]}))

    def test_numeric_pin_is_not_duplicated_in_prose(self):
        scenario = self.scenario()
        scenario["pinNote"] += " Enter 1234."
        self.assertTrue(profile_guidance_errors({"testScenarios": [scenario]}))

    def test_setup_limits_and_public_source_names_are_checked(self):
        for field, value in (("terminalSetup", []), ("knownLimitations", [""]), ("knownLimitations", ["BTT source"])):
            scenario = self.scenario()
            scenario[field] = value
            self.assertTrue(profile_guidance_errors({"testScenarios": [scenario]}))


if __name__ == "__main__":
    unittest.main()
