# Website structure and content contract

Static GitHub Pages content, with no application backend, analytics or build dependency.


<a id="README-site-structure"></a>
## Routes and assets

- [Home](../index.html) — HCE Test Tool, EMV Card Analyzer and ECR Test Tool
- [Developer guides](../guides/index.html) — application workflows and exchange-format reference
- [HCE Test Tool guide](../guides/hce-test-tool/index.html) — emulation, profile import, APDU diagnostics, history and reports
- [EMV Card Analyzer guide](../guides/emv-card-analyzer/index.html) — contactless reading, result states, trace import and export
- [ECR Test Tool guide](../guides/ecr-test-tool/index.html) — retained locally but omitted from navigation and sitemap
- [HCEImage JSON guide](../guides/hceimage-json/index.html) — shared envelope and distinct card-profile and analysis-trace payloads
- [HCE privacy policy](../hce-test-tool/privacy-policy/index.html)
- [EMV privacy policy](../emv-card-analyzer/privacy-policy/index.html)
- [ECR privacy policy](../ecr-test-tool/privacy-policy/index.html) — retained locally but omitted from navigation and sitemap
- [Shared styles](../assets/styles.css) and [sitemap](../sitemap.xml)


<a id="README-visual-and-content-conventions"></a>
## Visual and content conventions

All pages share one header, navigation, footer, typography, responsive card system, color tokens
and light/dark palette. Application icon PNGs preserve the distribution artwork. Keep the guide
cards, policy links and actions aligned across desktop and mobile widths. Use app-independent
language for diagnostic boundaries, use release numbers only for explicit compatibility requirements, and distinguish
document schema numbers from app versions.
Long HCE and JSON guides offer shortcut links under their introductions; keep the section
anchors stable because the in-app guidance and public links use them.

## Privacy policy ownership

Each HTML policy mirrors its application's `play/privacy-policy.md`, including meaningful
wording and effective dates. Hosting visitor-IP handling is separate from application data
processing. Policy changes require an intentional review of both copies; a documentation
reorganization does not change data practices or advance effective dates.

## Sources and authoring

Pages use semantic HTML and one shared stylesheet. Application icons retain distribution
artwork; tables/code remain readable at mobile widths. Internal links and anchors identify
actual routes, not application release numbers. Release-ready pages describe the matching prepared application version; deployment is gated separately in project records. JSON examples have independent
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
