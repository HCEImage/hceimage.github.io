# HCEImage website

Static GitHub Pages website for HCEImage applications, developer guidance and privacy policies.
It has no application backend, analytics or build dependency.

## Site structure

- [Home](index.html) — HCE Test Tool, EMV Card Analyzer and ECR Test Tool
- [Developer guides](guides/index.html) — application workflows and exchange-format reference
- [HCE Test Tool guide](guides/hce-test-tool/index.html) — emulation, profile import, APDU diagnostics, history and reports
- [EMV Card Analyzer guide](guides/emv-card-analyzer/index.html) — contactless reading, result states, trace import and export
- [ECR Test Tool guide](guides/ecr-test-tool/index.html) — retained locally but omitted from navigation and sitemap
- [HCEImage JSON guide](guides/hceimage-json/index.html) — shared envelope and distinct card-profile and analysis-trace payloads
- [HCE privacy policy](hce-test-tool/privacy-policy/index.html)
- [EMV privacy policy](emv-card-analyzer/privacy-policy/index.html)
- [ECR privacy policy](ecr-test-tool/privacy-policy/index.html) — retained locally but omitted from navigation and sitemap
- [Shared styles](assets/styles.css) and [sitemap](sitemap.xml)

## Local draft and publication boundary

The local site describes the prepared application functionality. It must not be published until the
corresponding application updates are available and the Play listings, availability links and policy
declarations have been checked. Editing or committing this repository does not publish the site;
publishing requires a separate push and successful GitHub Pages deployment.

The currently public HCE Play description still describes custom test security data as applying
only to the current run. Before publishing the revised website with the new build, update that
listing to distinguish the default one-use override from the optional keep-until-app-close choice
and to mention imported profile defaults accurately.

The HCE Google Play link points to its production listing. The EMV link points to its open-test
enrollment. ECR has no store action. The application cards identify supported platforms rather
than embedding app release numbers or treating distribution tracks as product capabilities.

## Privacy and effective dates

Each HTML policy must match its application's `play/privacy-policy.md`. The current effective dates
remain on the local draft pages because they identify the public policies already in force. Before
publishing revised wording, decide whether the change requires a new effective date and update the
HTML and corresponding application Markdown together. In particular, the revised HCE policy now
distinguishes persistent imported-profile defaults from temporary Emulator overrides; it must be
reviewed with the matching application release before publication. ECR policy wording is
status-neutral and includes local platform logs and Android's connection notification. EMV policy
correctly identifies Sessions as the release Logcat default.

GitHub Pages hosting is separate from application data processing. The policy pages identify
GitHub's visitor-IP handling and link its privacy statement.

## Visual and content conventions

All pages share one header, navigation, footer, typography, responsive card system, color tokens
and light/dark palette. Application icon PNGs preserve the distribution artwork. Keep the guide
cards, policy links and actions aligned across desktop and mobile widths. Use app-independent
language for diagnostic boundaries, avoid app release numbers in public copy, and distinguish
document schema numbers from app versions.

## Local verification

On 2026-10-01, the local pages were checked for app-version-free public wording, consistent
distribution links, shared styling, valid internal routes and anchors, and the absence of external
scripts or analytics. The HCE report disclosure was aligned with the application's Full evidence
and Redacted choices. HCE and EMV policy wording was compared with their Android manifests and
local data, backup, clipboard and export paths. This source review does not replace a visual browser
pass or the final Play Console privacy and Data safety review before publication.

Serve the root with `python3 -m http.server 8080 --bind 127.0.0.1` and open
`http://127.0.0.1:8080`. Check every page at desktop and phone widths in light and dark modes,
including navigation, focus states, readable tables, long code blocks, canonical URLs, image
loading, local links, privacy wording and sitemap entries. Verify that the in-app guidance URLs
match the guide routes here. Do not treat a local preview as public availability.
