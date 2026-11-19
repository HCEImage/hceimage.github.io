# Website structure and content contract

Static GitHub Pages content, with no application backend, analytics or build dependency.


<a id="README-site-structure"></a>
## Routes and assets

- [Home](../index.html) — HCE Test Tool and EMV Card Analyzer
- [Developer guides](../guides/index.html) — application workflows and exchange-format reference
- [HCE Test Tool guide](../guides/hce-test-tool/index.html) — emulation, profile import, APDU diagnostics, history and reports
- [EMV Card Analyzer guide](../guides/emv-card-analyzer/index.html) — contactless reading, result states, trace import and export
- [HCEImage JSON guide](../guides/hceimage-json/index.html) — shared envelope and distinct card-profile and analysis-trace payloads
- [HCE privacy policy](../hce-test-tool/privacy-policy/index.html)
- [EMV privacy policy](../emv-card-analyzer/privacy-policy/index.html)
- [Shared styles](../assets/styles.css) and [sitemap](../sitemap.xml)

The public application scope is limited to HCE Test Tool and EMV Card Analyzer. Only
their guides, policies and shared card-profile/analysis-trace reference are published.
The validator checks the complete seven-page inventory against the sitemap so an
unlinked HTML page cannot silently remain accessible.

## First-use navigation

The homepage distinguishes phone-as-card from phone-as-reader and links directly to each
single-presentation walkthrough. The guide index keeps application walkthroughs separate from
downloadable profiles and file-format specifications. Both application guides begin with
prerequisites, three quick-start steps and result review, before their detailed reference.
They share five primary shortcuts and an expandable chapter index. Profile selection/PIN/security
details in HCE and additional reading behavior in Analyzer remain available in expandable detail.

HCE's example uses the Built-in Mastercard No CVM / Signature below-limit scenario with profile
defaults and a matching authorized terminal/test-host setup. The 10 CZK example is conditional
on CZK and a 500 CZK reader CVM limit, not a terminal configuration command or approval promise.
Analyzer's example uses an authorized supported EMV test card, one presentation and no payment
PIN or external terminal. Each walkthrough separates captured evidence from payment acceptance.

The JSON page starts with complete downloadable profiles; envelope and payload specifications
remain available under their original anchors. Files and download URLs are unchanged. A
profile import and an analysis-trace import remain different workflows, and neither is required
for the basic walkthroughs.

## In-app guidance destinations

Public guides describe workflows and controls available in the released applications,
without requiring a particular arrangement or label for in-app web links. Keep the
existing guide roots, format reference, anchors and privacy URLs valid so installed
applications remain compatible.

The table below documents destinations for the locally prepared shared guidance links.
It does not imply that every released build exposes a link on every tab. New chapters
may be added before the corresponding app links are released; they remain useful
through the website itself. Preserve all of these anchors when reorganizing the guides:

| Application | Tab | Workflow chapter | Additional format reference |
| --- | --- | --- | --- |
| HCE Test Tool | Emulator | [Run a test](../guides/hce-test-tool/index.html#test-flow) | — |
| HCE Test Tool | Card profiles | [Import a card profile](../guides/hce-test-tool/index.html#import-profiles) | [Card profile format](../guides/hceimage-json/index.html#card-profile) |
| HCE Test Tool | History | [History and reports](../guides/hce-test-tool/index.html#history-reports) | — |
| HCE Test Tool | Settings | [Emulator and History settings](../guides/hce-test-tool/index.html#settings) | — |
| EMV Card Analyzer | Analyzer | [Run an analysis](../guides/emv-card-analyzer/index.html#analysis-flow) | — |
| EMV Card Analyzer | History | [History and reports](../guides/emv-card-analyzer/index.html#history-reports) | [Analysis trace format](../guides/hceimage-json/index.html#analysis-trace) |
| EMV Card Analyzer | Settings | [Analyzer and History settings](../guides/emv-card-analyzer/index.html#settings-safety) | — |

Privacy URLs remain independent of guidance and are unchanged. The HCE Settings chapter
describes existing controls without modifying privacy wording, policy dates or profile files.
Do not describe the new shared final link group or its exact action labels in public
HTML until doing so also matches the distributed applications.

`tools/check_site.py` resolves the current app-owned URLs from the two contextual-guidance
sources, HCE's profile-specific Test guidance and both privacy constants. The known Kotlin
literal/explicit tab-mapping forms are parsed without executing application code; an unresolved
fragment prefix is an error. The fixed `GUIDANCE_TARGETS`, `PUBLIC_ROUTES` and `PUBLIC_ANCHORS`
contracts separately retain older deployed destinations even when newer source changes.
`RELEASED_APPLICATION_TARGETS` additionally preserves the seven exact guide/format/privacy
destinations extracted from the released HCE and Analyzer runtime sources. In particular, HCE's
older unanchored JSON guide remains a valid page alongside its newer card-profile chapter link.
Visible chapter titles and section order may change, but these identifiers must not.
The HCE quick-start name, physical Mastercard identity and below-limit No CVM scenario are
also compared with the sibling application's native Built-in profile definition.

<a id="README-visual-and-content-conventions"></a>
## Visual and content conventions

All pages share one header, navigation, footer, responsive typography and spacing scale, card
system and light/dark palette. Use the full site width for catalogues and the same centered
reading column for application guides, the format reference and privacy policies. The shared
stylesheet defines spacing for paragraphs, headings, lists, callouts, captions and sections;
do not rely on browser-default margins or add page-specific offsets. Keep controls in download
cards aligned across columns. Only wide tables and code blocks should scroll horizontally.
Application icons preserve the distribution artwork. Use app-independent
language for diagnostic boundaries. Public pages describe shipped behavior without application
release numbers, private reference-tool names or roadmap copy. Use document schema numbers for
file compatibility. GitHub Pages excludes repository documentation and validation tools.
Both application guides and the JSON reference offer shortcut links under their introductions;
keep the section anchors stable because the in-app guidance and public links use them.
When changing the stylesheet, update its cache key consistently on all seven HTML pages.

Both homepage application cards keep Google Play as the sole primary action. Place the single-tap
walkthrough, full developer guide and privacy links together in one secondary row below it, in that
order. Allow the row to wrap on narrow screens rather than overflowing. Preserve the link destinations.

The homepage consistently shows the prepared Emulator and Analyzer, not completed results. Both first-use
guides use the same four-image progression: preparation, result, APDU timeline and decoded response.
Every thumbnail links directly to its full-size, unedited 1080 × 1920 native UI capture. Keep useful
alternate text, intrinsic dimensions, lazy loading and shared responsive gallery/caption styling.
Four columns become two on smaller screens without adding a carousel or JavaScript dependency.

HCE images must use the same physical Mastercard No CVM / Signature profile as the written
below-limit scenario, profile-default security and one presentation, not the two-tap Visa Mobile
Play journey. Analyzer's result, timeline and response show one synthetic multi-application analysis;
one presentation can read multiple applications. Captions distinguish generated UI fixtures from
physical NFC/host acceptance. Preserve the earlier `assets/hce-apdu-response.jpg` resource too.
Keep capture provenance in project verification rather than public application-version copy.
The checker guards screenshot order, full-size links, alt text, dimensions and both prepared homepage previews.

## Privacy policy ownership

Each HTML policy mirrors its application's `play/privacy-policy.md`, including wording and
effective date. The checker reads the current sibling HCE and EMV checkouts only. Before
publishing, verify that the mirrored policies describe the versions being distributed; identical
local copies do not establish that an app has been released. Hosting visitor-IP handling is
separate from application data processing. A documentation correction does not change data
practices or advance effective dates.

## Sources and authoring

Pages use semantic HTML and one shared stylesheet. Application icons retain distribution
artwork; tables/code remain readable at mobile widths. Internal links and anchors identify
actual routes, not application release numbers. Prepare HCE content for deployment with the
matching app release; keep EMV guide, trace and policy aligned with the already released Analyzer.
JSON examples have independent
envelope/payload versions and must remain valid native imports, not truncated illustrations.
The four physical downloads use payload 3 and derive from current Visa Online PIN, Mastercard Online PIN, Amex Adaptive CVM and JCB EMV Online PIN definitions.
Their Test guidance states amount-independent or separate below/above-reader-limit scenarios, structured
PIN references, concrete setup, temporary-key/Keep/Reset boundaries and reader/host limitations. Visa/MC fixed Online PIN requests remain explicit even below the reader limit.
Public source metadata is CUSTOM only. Guidance edits do not alter an existing imported snapshot.
Mastercard custom application overrides require the complete MK-AC/MK-IDN group and retain the
matching ICC key/certificates for CDA; the Amex example includes its matching synthetic ICC signing key and requested CDA support.
The web checker validates guidance completeness, one download action per example, public source-name exclusion, CUSTOM-only provenance and policy body/effective-date parity, while HCE integration tests validate actual
import, payload-3 parity with Built-in processing, APDU flows, dynamic cryptograms, requested Mastercard/Amex/JCB CDA, custom/Reset and PIN display.

## Technical navigation

- [Technical documentation](README.md) — current specifications and module contracts.
