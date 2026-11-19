"""Small parser regressions; run with python3 -m unittest discover -s tools."""

import unittest

from check_site import (
    GUIDANCE_TARGETS,
    PUBLIC_ANCHORS,
    PUBLIC_EXAMPLES,
    PUBLIC_ROUTES,
    RELEASED_APPLICATION_TARGETS,
    WALKTHROUGH_IMAGES,
    Page,
    application_target_errors,
    application_targets,
    example_download_errors,
    example_inventory_errors,
    guidance_target_errors,
    has_external_source_name,
    markdown_effective_date,
    markdown_policy,
    normalized_text,
    profile_guidance_errors,
    public_copy_errors,
    public_anchor_errors,
    quick_start_errors,
    quick_start_profile_errors,
    route_inventory_errors,
    walkthrough_image_errors,
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


class WalkthroughImageTest(unittest.TestCase):
    def pages(self):
        return {
            "/": Page('<a href="/assets/hce-single-tap-emulator.jpg">Emulator</a>'
                      '<a href="/assets/emv-single-tap-ready.jpg">Analyzer</a>'),
            **{
                route: Page('<div class="walkthrough-gallery">' + "".join(
                    f'<figure><a href="{source}"><img src="{source}" alt="Example UI" '
                    'width="1080" height="1920"></a></figure>' for source in images
                ) + '</div>')
                for route, images in WALKTHROUGH_IMAGES.items()
            },
        }

    def test_both_native_image_sequences_have_clickable_full_size_links(self):
        self.assertEqual([], walkthrough_image_errors(self.pages()))

    def test_missing_or_reordered_step_is_rejected(self):
        pages = self.pages()
        pages["/guides/hce-test-tool/"].walkthrough_images.reverse()
        self.assertIn("order", walkthrough_image_errors(pages)[0])

    def test_unlinked_thumbnail_is_rejected(self):
        page = Page('<div class="walkthrough-gallery"><img src="/screen.jpg" alt="UI" '
                    'width="1080" height="1920"></div>')
        pages = self.pages()
        pages["/guides/emv-card-analyzer/"] = page
        self.assertTrue(any("full-size link" in error for error in walkthrough_image_errors(pages)))

    def test_missing_alt_or_dimensions_is_rejected(self):
        pages = self.pages()
        page = pages["/guides/hce-test-tool/"]
        source = page.walkthrough_images[0][0]
        page.walkthrough_images[0] = (source, source, "", "540", "960")
        self.assertTrue(any("native dimensions" in error for error in walkthrough_image_errors(pages)))

    def test_homepage_does_not_fall_back_to_a_decoded_response(self):
        pages = self.pages()
        pages["/"] = Page('<img src="/assets/hce-apdu-response.jpg">')
        self.assertIn("Homepage", walkthrough_image_errors(pages)[0])

    def test_homepage_analyzer_does_not_fall_back_to_a_completed_result(self):
        pages = self.pages()
        pages["/"] = Page('<img src="/assets/hce-single-tap-emulator.jpg">'
                          '<img src="/assets/emv-analysis-summary.jpg">')
        self.assertEqual(["Homepage EMV preview must show the prepared Analyzer"],
                         walkthrough_image_errors(pages))


class PublicSourceNameTest(unittest.TestCase):
    def test_external_name_is_rejected_in_copy_paths_and_metadata(self):
        for value in ("BTT", "btt", "BTT_CARD_IMAGE", "archive/Btt/profile.xml", "Brand Test Tool"):
            self.assertTrue(has_external_source_name(value))
        self.assertFalse(has_external_source_name('{"source":{"format":"CUSTOM"}}'))


class PublicCopyTest(unittest.TestCase):
    def test_cash_register_copy_and_metadata_are_rejected(self):
        for copy in (
            "ECR Test Tool", "Electronic cash register simulation", "cash-register simulators",
            "nexo Retailer", "Local POI", '<img src="/assets/ecr-test-tool.png">',
        ):
            with self.subTest(copy=copy):
                self.assertTrue(public_copy_errors(copy))

    def test_card_emulation_and_host_simulators_remain_in_scope(self):
        self.assertEqual([], public_copy_errors(
            "EMV card emulation, APDU diagnostics and an authorized test host simulator."
        ))

    def test_app_release_numbers_and_roadmap_status_are_rejected(self):
        for copy in ("HCE Test Tool 1.0.0", "v0.2.0", "Roadmap", "In development", "Coming soon"):
            with self.subTest(copy=copy):
                self.assertTrue(public_copy_errors(copy))

    def test_wire_schema_and_authorized_development_language_are_preserved(self):
        self.assertEqual([], public_copy_errors("Payload schema 3. Authorized development only."))


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


class GuidanceDestinationTest(unittest.TestCase):
    def pages(self):
        sections = {}
        for target in GUIDANCE_TARGETS:
            route, anchor = target.split("#")
            sections.setdefault(route, []).append(f'<h2 id="{anchor}">Chapter</h2>')
        return {route: Page("".join(headings)) for route, headings in sections.items()}

    def test_all_primary_tabs_and_format_references_have_real_chapters(self):
        self.assertEqual([], guidance_target_errors(self.pages()))

    def test_missing_settings_anchor_is_reported(self):
        pages = self.pages()
        page = pages["/guides/hce-test-tool/"]
        page.ids.remove("settings")
        self.assertEqual(
            ["Missing in-app guidance destination: /guides/hce-test-tool/#settings"],
            guidance_target_errors(pages),
        )

    def test_missing_format_page_is_reported(self):
        pages = self.pages()
        del pages["/guides/hceimage-json/"]
        self.assertEqual(2, len(guidance_target_errors(pages)))


class PublicAnchorTest(unittest.TestCase):
    def pages(self):
        return {
            route: Page("".join(f'<h2 id="{anchor}">Content</h2>' for anchor in anchors))
            for route, anchors in PUBLIC_ANCHORS.items()
        }

    def test_all_preexisting_public_fragments_remain_supported(self):
        self.assertEqual([], public_anchor_errors(self.pages()))

    def test_an_older_format_fragment_is_not_removed_during_reordering(self):
        pages = self.pages()
        pages["/guides/hceimage-json/"].ids.remove("legacy-security")
        self.assertEqual(
            ["Missing stable public anchor: /guides/hceimage-json/#legacy-security"],
            public_anchor_errors(pages),
        )

    def test_privacy_fragments_remain_independent_of_guidance(self):
        pages = self.pages()
        del pages["/emv-card-analyzer/privacy-policy/"]
        self.assertEqual(10, len(public_anchor_errors(pages)))


class ApplicationLinkSourceTest(unittest.TestCase):
    def test_direct_guide_and_policy_urls_are_read_without_execution(self):
        urls, errors = application_targets(
            'val guide = "https://hceimage.github.io/guides/hce-test-tool/"\n'
            'val policy = "https://hceimage.github.io/hce-test-tool/privacy-policy/"'
        )
        self.assertEqual([], errors)
        self.assertEqual({
            "https://hceimage.github.io/guides/hce-test-tool/",
            "https://hceimage.github.io/hce-test-tool/privacy-policy/",
        }, urls)

    def test_kotlin_tab_mapping_expands_each_actual_fragment(self):
        urls, errors = application_targets('''
            get() = "https://hceimage.github.io/guides/hce-test-tool/#" + when (this) {
                ScreenGuidance.Emulator -> "test-flow"
                ScreenGuidance.Settings -> "settings"
            }
        ''')
        self.assertEqual([], errors)
        self.assertEqual({
            "https://hceimage.github.io/guides/hce-test-tool/#test-flow",
            "https://hceimage.github.io/guides/hce-test-tool/#settings",
        }, urls)

    def test_unrecognized_fragment_construction_is_not_silently_skipped(self):
        urls, errors = application_targets('"https://hceimage.github.io/guides/hce-test-tool/#" + other')
        self.assertEqual(set(), urls)
        self.assertEqual(1, len(errors))

    def test_changed_app_destination_must_exist_on_the_website(self):
        pages = {"/guides/hce-test-tool/": Page('<h2 id="test-flow">Quick start</h2>')}
        self.assertEqual([], application_target_errors({
            "https://hceimage.github.io/guides/hce-test-tool/#test-flow",
        }, pages))
        self.assertEqual(2, len(application_target_errors({
            "https://hceimage.github.io/guides/hce-test-tool/#renamed",
            "https://hceimage.github.io/hce-test-tool/privacy-policy/",
        }, pages)))


class ReleasedApplicationLinkTest(unittest.TestCase):
    def pages(self):
        return {
            route: Page("".join(f'<h2 id="{anchor}">Content</h2>' for anchor in anchors))
            for route, anchors in PUBLIC_ANCHORS.items()
        }

    def test_production_binaries_keep_all_seven_original_destinations(self):
        self.assertEqual(7, len(RELEASED_APPLICATION_TARGETS))
        self.assertEqual([], application_target_errors(RELEASED_APPLICATION_TARGETS, self.pages()))

    def test_older_hce_format_root_still_requires_a_real_page(self):
        pages = self.pages()
        del pages["/guides/hceimage-json/"]
        self.assertIn("Missing application link destination: https://hceimage.github.io/guides/hceimage-json/",
                      application_target_errors(RELEASED_APPLICATION_TARGETS, pages))

    def test_production_history_fragment_cannot_be_renamed(self):
        pages = self.pages()
        pages["/guides/hce-test-tool/"].ids.remove("history-reports")
        self.assertEqual([
            "Missing application link destination: https://hceimage.github.io/guides/hce-test-tool/#history-reports",
        ], application_target_errors(RELEASED_APPLICATION_TARGETS, pages))


class QuickStartTest(unittest.TestCase):
    def pages(self):
        pages = {}
        for route, flow, result, settings in (
            ("/guides/hce-test-tool/", "test-flow", "inspect-exchange", "settings"),
            ("/guides/emv-card-analyzer/", "analysis-flow", "result-states", "settings-safety"),
        ):
            targets = ["before-starting", flow, result, "history-reports", settings]
            shortcuts = '<nav aria-label="Guide shortcuts">' + "".join(
                f'<a href="#{target}">{target}</a>' for target in targets
            ) + '</nav>'
            sections = "".join(f'<section aria-labelledby="{target}"></section>' for target in targets)
            steps = '<ol class="quick-start-steps"><li>Prepare</li><li>Present</li><li>Review</li></ol>'
            pages[route] = Page(shortcuts + sections + steps)
        return pages

    def test_both_guides_share_the_same_first_use_progression(self):
        self.assertEqual([], quick_start_errors(self.pages()))

    def test_advanced_catalog_cannot_move_ahead_of_the_first_test(self):
        pages = self.pages()
        pages["/guides/hce-test-tool/"].section_ids.insert(0, "development-profiles")
        self.assertEqual(1, len(quick_start_errors(pages)))

    def test_missing_steps_or_asymmetric_shortcuts_are_reported(self):
        pages = self.pages()
        page = pages["/guides/emv-card-analyzer/"]
        page.shortcut_targets.pop()
        page.quick_start_steps = 2
        self.assertEqual(2, len(quick_start_errors(pages)))


class QuickStartProfileTest(unittest.TestCase):
    def profile(self):
        return {
            "id": "mastercard-physical-emv-no-cvm-signature", "brand": "MASTERCARD",
            "name": "Mastercard No CVM / Signature", "formFactor": "PHYSICAL",
            "testScenarios": [{"amountCondition": "BELOW_CVM_LIMIT", "expectedCvm": "NO_CVM"}],
        }

    def test_first_test_uses_the_real_named_physical_no_cvm_scenario(self):
        self.assertEqual([], quick_start_profile_errors(self.profile(), "Mastercard No CVM / Signature"))

    def test_source_changes_cannot_silently_make_the_walkthrough_inaccurate(self):
        for field, value in (
            ("name", "Renamed profile"), ("formFactor", "TOKENIZED"),
            ("brand", "VISA"), ("testScenarios", [{"amountCondition": "ANY", "expectedCvm": "ONLINE_PIN"}]),
        ):
            profile = self.profile()
            profile[field] = value
            with self.subTest(field=field):
                self.assertTrue(quick_start_profile_errors(profile, "Mastercard No CVM / Signature"))


class RouteInventoryTest(unittest.TestCase):
    def test_supported_pages_match_the_sitemap(self):
        self.assertEqual([], route_inventory_errors(PUBLIC_ROUTES, list(PUBLIC_ROUTES)))

    def test_unlinked_extra_page_cannot_remain_published(self):
        routes = set(PUBLIC_ROUTES) | {"/guides/retired-tool/"}
        self.assertTrue(route_inventory_errors(routes, list(PUBLIC_ROUTES)))

    def test_missing_or_duplicate_sitemap_routes_are_rejected(self):
        routes = sorted(PUBLIC_ROUTES)
        self.assertTrue(route_inventory_errors(PUBLIC_ROUTES, routes[:-1]))
        self.assertTrue(route_inventory_errors(PUBLIC_ROUTES, routes + routes[:1]))

    def test_missing_or_duplicate_public_pages_are_rejected(self):
        routes = sorted(PUBLIC_ROUTES)
        self.assertTrue(route_inventory_errors(routes[:-1], routes))
        self.assertTrue(route_inventory_errors(routes + routes[:1], routes))


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
