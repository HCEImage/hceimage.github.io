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

## Current publication status

The owner confirmed HCE Test Tool approval and production publication on 2026-10-01. Its native
profile-import functionality, updated listing and screenshots are released. The previously
published guides and policies accompany that release. The follow-up website update adds visible
format-specification entry points and three downloadable, validated synthetic profile examples.
No app release numbers appear in public website copy. EMV remains in open testing; ECR has no
store action and its retained guide/policy routes remain absent from navigation and sitemap.

Production publication does not establish that an existing device has received its in-place
Play update; that preservation check remains tracked in the HCE release documentation.

## Publication procedure

The site describes the prepared application functionality. Before publication, check the
matching application artifacts, Play listing, availability links and policy declarations. For the
coordinated HCE update, save the store listing and signed bundle in Play Console first, publish the
matching guides and privacy policy, then submit the prepared Console changes for review. A prepared
Console release is not a publicly available update. Editing or committing this repository does not
publish the site; publishing requires a separate push and successful GitHub Pages deployment.

The published HCE Play description and screenshots include native profile import and distinguish
persistent imported-profile defaults from the default one-use Emulator override and the optional
keep-until-app-close choice. Record application publication only with actual confirmation from
the owner or Play Console, not merely because store assets or a bundle have been saved.

The HCE Google Play link points to its production listing. The EMV link points to its open-test
enrollment. ECR has no store action. The application cards identify supported platforms rather
than embedding app release numbers or treating distribution tracks as product capabilities.

## Privacy and effective dates

Each HTML policy must match its application's `play/privacy-policy.md`. The policies prepared for
publication on 2026-10-01 use October 1, 2026 as their effective date, aligned with the corresponding
application Markdown. Future wording changes must be reviewed for an effective-date update in
both copies together. In particular, the revised HCE policy now
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

## Verification history

The entries below record the state at each review/publication step. References to drafts or pending
application review describe those earlier steps, not the current owner-confirmed production status.

On 2026-10-01, the local pages were checked for app-version-free public wording, consistent
distribution links, shared styling, valid internal routes and anchors, and the absence of external
scripts or analytics. The HCE report disclosure was aligned with the application's Full evidence
and Redacted choices. HCE and EMV policy wording was compared with their Android manifests and
local data, backup, clipboard and export paths. This source review does not replace a visual browser
pass or the final Play Console privacy and Data safety review before publication.

The subsequent Common integration review aligned the JSON guide with strict required-field types:
string format/kind, integer-number envelope schema and object payload. Missing/null or incorrectly
typed required fields are rejected without changing valid exported documents. Application guides
already describe the current profile/trace workflows; no new feature or privacy-date change was
needed. Public pages remain free of concrete application release numbers, and no visual assets,
shared styles, availability links or hidden ECR navigation were changed. The site remains a local
draft; this review does not publish it.

Serve the root with `python3 -m http.server 8080 --bind 127.0.0.1` and open
`http://127.0.0.1:8080`. Check every page at desktop and phone widths in light and dark modes,
including navigation, focus states, readable tables, long code blocks, canonical URLs, image
loading, local links, privacy wording and sitemap entries. Verify that the in-app guidance URLs
match the guide routes here. Do not treat a local preview as public availability.

### Final local website review — 2026-10-01

All nine HTML pages, including the retained ECR pages, were rendered in an isolated Chrome browser
at 360, 768 and 1440 CSS pixels in light and dark modes (54 renders). Automated checks found no
page-level horizontal overflow, missing images, HTTP errors, JavaScript errors or broken internal
routes/anchors. All pages retain a single primary heading, shared stylesheet and version-free
application wording. The full-page visual overview confirmed consistent cards, navigation,
typography and light/dark colors. Format tables scroll inside their own region on narrow screens;
JSON examples and tables are keyboard-focusable. The stylesheet cache key is consistent across
all pages.

The specification discoverability follow-up adds matching reference cards to the HCE profile-import
and EMV trace workflows, plus direct card-profile and analysis-trace buttons in the Exchange formats
overview. Both link to anchors in the existing shared specification without duplicating it.
The cards reuse the shared card and button styles, with
wrapping labels for narrow screens. The follow-up stylesheet cache key is `20261001-3` on all pages.

The JSON guide contains three downloadable contactless online examples under
`guides/hceimage-json/examples/`: Visa, Mastercard and American Express. Their separate
`web-example-…-online-pin` IDs avoid the bundled catalog and supersede the minimal label-only
scripts. These examples adapt the bundled, terminal-oriented APDU flows and include coherent
PAN/Track 2 data, DOL inputs and public demonstration security defaults. Visa and Amex have newly
invented test PANs. Mastercard retains its already-public synthetic PAN, artificial ICC RSA key
and matching test certificate records so that changing a PAN does not break signed dependencies.
All application-cryptogram keys are the public demonstration key with KCV 08D7B4; Mastercard's
dynamic-number key has KCV FB0975. No production credentials or device-session data are included.
Provenance identifies the bundled starting point, not a claim of certification or authenticity.

The guide explains download/import, small/above-CVM-limit test transactions, test PINs, terminal
card/BIN configuration, host-key requirements, and required/optional/conditional field groups.
JSON comments and extra annotation fields are deliberately excluded because the importer rejects
them. Annotations live in the field reference and supported descriptions/scenario guidance.
Download actions and raw-file viewing links reuse the shared card/button system. The HCE guide and
formats overview link directly to examples. The files pass the actual JVM import validator with
no warnings, reject duplicate IDs and incorrect KCVs, and complete 4/9/11 APDUs respectively with
9000, final Success and successful local session checks. This does not establish host approval,
test CA configuration or compatibility with every physical terminal; the final modified files
were subsequently tested by the owner on the connected Samsung and test terminal: import and
emulation passed for all three. This reports the manual test, not a guarantee of other terminal
configurations or host approval. Display names are Visa example, Mastercard example and American
Express example; removing “terminal” from the names does not change Profile IDs or behavior.

The guide review checked the HCE native-profile validator and private no-backup store, EMV trace
documentation and History controls, ECR architecture and TCP transport, shared format rules, and
in-app guide URLs. HCE guidance now explains APDU timing boundaries, deletion without erasing old
sessions, and repeating a session's Profile ID dependency. EMV guidance names report formats and
History filtering/Undo. Both guides caution that Redacted exports are not an anonymity guarantee.
The retained ECR policy now distinguishes Android uninstall cleanup from desktop data that may
remain after uninstalling; the matching ECR Markdown policy was updated together with the HTML.
All three HTML policies were compared with their application's Markdown policy; dates remain draft
dates pending the separately authorized publication step. Update the effective date of revised
policy wording and its matching Markdown on publication, not merely on local review. Icon artwork,
store track destinations and hidden ECR navigation remain unchanged. No push or Pages deployment
was performed as part of this review.

## Publication preparation — 2026-10-01

The owner authorized publication after completing the local website review and preparing the HCE
listing, screenshots, release notes and signed bundle in Play Console. Updated guides and privacy
pages are published independently of the application review. HCE's Play update is still pending;
website publication does not establish that the new application is available on Google Play.
All revised policies use the publication date in both HTML and their application Markdown copies.
The retained ECR pages remain omitted from navigation and sitemap. Confirm live page content after
the Pages deployment before submitting the Console changes for review.

## Production follow-up — 2026-10-01

The owner confirmed application approval/publication and authorized this follow-up website
deployment. All nine pages passed another 54-render check at 360/768/1440 pixels in light/dark
modes, with no broken internal links, missing images, page overflow or browser errors. The example
cards were visually inspected in desktop light and phone dark layouts. Actual browser downloads
return the three expected `.hceimage.json` filenames and match the reviewed local bytes. All three
files pass native import, duplicate-ID/KCV rejection and complete engine/session validation.
Privacy text and dates match all three application Markdown copies. No policy wording change was
needed for the public synthetic examples; hosting remains separate from application processing.

## EMV publication follow-up — 2026-10-05

The owner confirmed approval and complete EMV open-testing publication. The trace specification
now uses `payload.schemaVersion` in its structure, with one sentence explaining that import also
accepts legacy `payload.payloadVersion`. Detailed compatibility rules stay in the application's
technical documentation. The EMV guide explains Card response exchange timing, overall Duration,
missing measurements and the restriction on exporting an imported Redacted trace.

Before this follow-up, all nine live HTML pages, the shared stylesheet, sitemap and three
synthetic downloadable profile examples matched the repository byte for byte. All 79 internal
references resolved, the three examples parsed with envelope/payload schema 1, and no application
release numbers appeared in public HTML. Home, availability links and all three policy texts were
reviewed against the application documentation. Privacy wording and October 1 dates remain unchanged;
ECR routes remain absent from navigation and sitemap. Deployment of this follow-up is separate
from application publication and must be verified after push.
