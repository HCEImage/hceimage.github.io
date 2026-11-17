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
Long HCE and JSON guides offer shortcut links under their introductions; keep the section
anchors stable because the in-app guidance and public links use them.
When changing the stylesheet, update its cache key consistently on all seven HTML pages.

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
