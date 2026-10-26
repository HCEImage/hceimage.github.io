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
language for diagnostic boundaries, avoid app release numbers in public copy, and distinguish
document schema numbers from app versions.

## Privacy policy ownership

Each HTML policy mirrors its application's `play/privacy-policy.md`, including meaningful
wording and effective dates. Hosting visitor-IP handling is separate from application data
processing. Policy changes require an intentional review of both copies; a documentation
reorganization does not change data practices or advance effective dates.

## Sources and authoring

Pages use semantic HTML and one shared stylesheet. Application icons retain distribution
artwork; tables/code remain readable at mobile widths. Internal links and anchors identify
actual routes, not application release numbers. Development-preview notices distinguish
unreleased features from published application capabilities. JSON examples have independent
envelope/payload versions and must remain valid native imports, not truncated illustrations.

## Technical navigation

- [Technical documentation](README.md) — current specifications and module contracts.
