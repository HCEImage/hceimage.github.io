# HCEImage website verification

Repeatable validation procedures and retained execution evidence. Dated checkpoints describe
their own stage, not a current capability promise. The technical contract remains authoritative;
software checks, physical interoperability and host/certification acceptance are different gates.

<a id="emv-021-guide-publication"></a>
## EMV maintenance guide publication — 2026-11-20

The owner explicitly authorizes publication of the prepared guide. Push website content commit
`9e56f56a9196c17b416a1b914bbc754522cf5c64` to `origin/main`; the existing GitHub Pages
[build and deployment](https://github.com/HCEImage/hceimage.github.io/actions/runs/44721301666) completes successfully.
The EMV guide is live at <https://hceimage.github.io/guides/emv-card-analyzer/> with Cirrus,
separate Discover ZIP scope, known D-PAS IAD interpretation and corrected APDU navigation.

Independently fetch all 27 public files over HTTPS after deployment. Every file matches the
prepared commit byte-for-byte: seven HTML pages, fourteen assets, four profile downloads,
sitemap and robots file. Unqueried canonical homepage and EMV guide responses also match,
so the result does not depend solely on a cache-busting query or an HTTP 200 status.

All fourteen distinct current/released application destinations resolve against the actual live
HTML, with all 59 previous fragment IDs preserved. The two Play privacy URLs retain their
published routes, bodies and effective dates. The homepage, HCE guide, trace reference,
shared CSS, images and downloadable JSON files are unchanged. The pre-publication validator
and all 52 tests pass. Raw HTTP/hash evidence is retained privately outside the repository.

Publish only the prepared website commit. Application/Common source, signed AABs and their
release status are unchanged by this operation; app approval and production upgrade acceptance
are tracked separately in the Analyzer project. Record this successful deployment in a local
documentation commit without an additional push or second content deployment.

<a id="emv-021-guide-preparation"></a>
## Prepared EMV maintenance guide update — 2026-11-20

Prepare the owner-approved guide changes for EMV 0.2.1 while retaining the published website
baseline at `88e2e4b64284a231a31988ee14925619f7318b73`. Add Cirrus to Mastercard support and
separate advertised Discover ZIP data reading from modern D-PAS/Book C-6. Document its AFL,
Track 1/2 and optional unverified DCVV limits, including malformed-data Incomplete outcomes.
Explain recognized D-PAS IAD CVN 15/16 decoding without cryptographic verification and preserve
unknown variants/fields. Correct the quick-start, gallery caption and inspection instructions:
Details expands an application, while APDU exchange is below the result and optional note.

Review the wording against the checked-in analyzer reading/findings contracts and the Common
IAD implementation. The public guide describes current functionality without application release
numbers, roadmap status or external test-tool names. This record alone carries release timing.
No privacy-policy body/date, trace schema/reference, homepage, CSS, image or downloadable profile
changes are needed. Application and Common sources, binaries and runtime link strings are unchanged.

Static validation passes for seven HTML pages, 135 local references, four profile envelopes,
JSON illustrations and two exact application/privacy mirrors. All 52 checker tests pass.
Compare with the pre-edit Git baseline: every public route and all 59 actual fragment IDs
are identical, including the fixed 56-fragment compatibility baseline. Resolve all twelve
current-source destinations and independently extract seven released destinations from HCE
`79a26e7` and Analyzer `aaeb5c171d0031abe13a8757da73d2782c46ddea`: fourteen unique app targets,
all valid. The twelve localized Play listing files retain their two policy URLs, which resolve
unchanged; this checks repository copy/URL compatibility, not authenticated Console settings.

All non-guide public files are byte-identical to the baseline. No navigation destination,
heading ID, privacy URL, download name or schema version is changed. Shared presentation and
existing gallery behavior remain intact; this text/table update does not repeat the earlier
full responsive browser sweep. Commit locally without pushing. Publication stays pending until
EMV 0.2.1 production availability is confirmed and a deployment is authorized and verified.

## Single-presentation website deployment — 2026-11-19

The owner-authorized website content commit `36de02b602836b51eb19a3bc1d6e01ca5eab607a` was
pushed to `origin/main` and is live at [HCEImage](https://hceimage.github.io/). All 27 public files
match that commit byte-for-byte over HTTPS: seven HTML routes, fourteen shared assets, four
native profile downloads, sitemap and robots file. The canonical homepage also matches without
an audit query parameter. Maintenance README, project verification and checker endpoints are
not published (HTTP 404).

The deployed HTML resolves all fourteen distinct current/production application destinations.
Browser navigation confirms both homepage quick-start links, the four-image guides, unchanged
JSON guide root, card-profile/trace anchors and four downloads. The prepared Emulator/Analyzer
previews and three-link rows render on the public homepage. This is verified publication, not
merely a successful Git push. HCE, Analyzer and Common source/checkouts are unchanged by this work.

## Single-presentation guide review — 2026-11-19

Local static validation covers seven HTML pages, 135 local references, four unchanged profile
files and two unchanged policy bodies/effective dates. All 52 checker tests pass, including six
gallery regressions for screenshot order, full-size links, alt text, dimensions and homepage role.
The compatibility baseline retains all 56 existing public fragment IDs and all seven routes.
Twelve current app destinations are
resolved from the five HCE/EMV Kotlin guidance/privacy sources; older roots and chapter links
remain separately guarded. The selected native HCE Mastercard physical No CVM/Signature
profile substantiates the walkthrough's name and below-limit No CVM scenario.

Production-source comparison independently covers HCE 1.0.0 (16), runtime baseline `79a26e7`,
and Analyzer 0.2.0 (6), baseline `aaeb5c171d0031abe13a8757da73d2782c46ddea` from the retained
release records/candidate metadata. All seven unique released targets remain valid, including
HCE's unanchored JSON guide and History fragment. The checker now retains this exact production
URL set, with three regression tests, independently of the twelve current-source targets.
Both production privacy sources byte-match the current application policies, and both website
mirrors retain their original wording and effective dates. No application source is modified.

The final browser review covers all seven pages at 320, 390, 768 and 1365 CSS pixels (28 layouts)
in the active dark palette, with one H1, 16-pixel body text, no horizontal page overflow and no
broken visible images. All fourteen distinct current/production destinations resolve to their
intended page/chapter at 390 pixels. Both guides
have five matching shortcut roles and three quick-start steps before advanced reference.
Expandable chapter navigation, retained HCE PIN/security explanations, Analyzer read details
and the four download/view pairs are present. This is website/source compatibility review,
not a new physical NFC, terminal/host or app-installation acceptance run.

Both prepared homepage images and the secondary link rows retain the owner-approved arrangement;
the three guide/privacy actions sit below the sole Google Play button, wrapping only on narrow
screens. Expanded chapter/PIN/read-details panels and both full-size decoded-response image links
work. Both Play listing URLs and the GitHub privacy-statement URL return HTTP 200. All 56 preexisting
fragments and all four native download bytes match the prior website commit. Shared CSS cache
identity is advanced consistently on all seven pages. No script, backend, analytics or new
application behavior is added.

The initial homepage JPEGs remain available under their original asset URLs:

- HCE `phone-05-apdu-response.jpg`, now `assets/hce-apdu-response.jpg` — SHA-256 `a35a4b8001999717d7777e284ec9fa9dd2bc8a33b3ffd4370dde6219e6fa47b4`
- EMV `phone-01-analysis-summary.jpg`, now `assets/emv-analysis-summary.jpg` — SHA-256 `fddfe2201bf303725660554ef9b492b14f3369596de5b87d72847c04efb90475`

The homepage pairs `assets/hce-single-tap-emulator.jpg` with `assets/emv-single-tap-ready.jpg`:
both show the prepared workspace and its Start action. Results remain in the guide walkthroughs.
Four new HCE captures use the
actual bundled physical Mastercard No CVM / Signature profile, profile-default security, a
10 CZK software input, No CVM CDOL evidence and a requested-CDA first ARQC. The real engine
processes nine commands and passes all six profile checks. No retry scenario or first/second
presentation grouping is present. These captures show Emulator, History summary, ordered APDUs
and the decoded GPO response; they are not physical NFC or host-authorization evidence.

Analyzer adds a clean prepared screen and a response capture scrolled to the decoded AIP/AFL.
Its masked result and timeline are unchanged copies of `play/assets/phone-01-analysis-summary.jpg`
and `phone-02-apdu-exchange.jpg`; the response uses that same deterministic multi-application
fixture. All gallery images link to their full native 1080 × 1920 files, with no stitching or
image editing. Public captions explain the synthetic example boundary.

The Samsung capture runs use temporary test-only classes and the isolated `.screenshots`
application/test packages; both final runs report `OK (1 test)`. Ordinary installations and
history are not read or replaced. Capture packages and temporary test sources are removed, and
the original 1080 × 2340 display size and density 450 are restored without overrides. Application
and Common source are untouched. These initial captures were reviewed locally without a commit
or publication. The owner subsequently approved the final layout and authorized the website
commit and publication after the final whole-site and production-link checks.

## Contextual guidance destinations — 2026-11-17

The HCE guide adds the Settings chapter describing existing controls, defaults and privacy
entry points. Both public guides describe workflows and separate file-format specifications
without prescribing the locally prepared guidance footer or new action labels. Existing
guide roots and anchors remain compatible with installed production HCE and EMV apps;
the additional Settings anchor does not require an application update. The local technical
documentation distinguishes prepared app-link destinations from released UI behavior.
Static validation passes for seven pages, 80 local references, four profile files and
two unchanged privacy-policy mirrors. All 31 checker tests pass, including
the nine in-app chapter/format destinations and missing-target regressions.
Chrome covers all seven pages at 320, 768 and 1440 pixels in light/dark modes and at
200% text on a 360-pixel viewport in both modes: 56 combinations without horizontal
overflow or broken content images. The new Settings section was visually reviewed at
phone and desktop widths. Shared CSS, privacy bodies/dates and profile downloads are unchanged.
The owner subsequently authorized publication of this backward-compatible web update
independently of the prepared app changes. Verify the matching Pages deployment and live
chapter anchors after pushing; HCE, EMV and Common changes remain uncommitted.

## Public application scope — 2026-11-17

Local static validation passes for seven HTML pages, 78 local references, four native
profile downloads and two exact privacy-policy mirrors. All 28 checker tests pass,
including removed-scope copy and complete HTML/sitemap inventory regressions.
The two remaining policies, four JSON downloads, HCE/EMV guides and shared stylesheet
retain their previous bytes. The homepage now describes only card emulation, card analysis
and APDU diagnostics.

An isolated Chrome review covers all seven pages at 320, 768 and 1440 CSS pixels in
light and dark modes, plus all pages at 200% text and 360 pixels in both modes:
56 combinations without horizontal page overflow or broken content images. All pages
retain one H1 and return HTTP 200. The mobile dark and desktop light homepage screenshots
were visually reviewed. The browser's optional, pre-existing favicon.ico fallback is
excluded from content-resource failures; no stylesheet or icon redesign is introduced.

The owner explicitly authorized commit, push and GitHub Pages publication after these checks.
Deployment completion must be verified independently of the successful local preview.

## Shared visual consistency — 2026-11-16

Chrome covers all nine HTML routes at 320, 360, 768, 1024 and 1440 pixels in both color
schemes (90 renders), plus all routes at 200% text on a 360-pixel screen. Check consistent
paragraph, adjacent-note and section spacing, keyboard focus, download alignment and ordinary
text/link contrast of at least 4.5:1. The page does not scroll horizontally, images load, and
the four local download actions still return valid profile envelopes. Review representative
screenshots of the catalogue, guides, policies and examples. This is a layout-only update:
policy wording and dates, navigation destinations, artwork and JSON remain unchanged.

## HCE production website deployment — 2026-11-16

[GitHub Pages run 43856976306](https://github.com/HCEImage/hceimage.github.io/actions/runs/43856976306)
completed successfully for content commit `d44260f` after the owner confirmed the matching
Play release. All nine HTML routes, four JSON downloads, seven shared assets, sitemap and
robots file matched the committed bytes over HTTPS. All three policies were included in the
comparison. The repository README, project verification record and validator script returned
HTTP 404 on the Pages origin as expected.

## HCE production website handoff — 2026-11-16

PASS: nine HTML routes, 91 local references, four profile downloads and three policy mirrors,
including dates and policy bodies. All 22 checker tests pass. The Analyzer mirror matches the
policy shipped with the current Play release; its guide and format reference describe trace
payload 1. HCE still uses profile payload 3 and keeps its simulated-verification policy.
HCE policy wording and dates did not change in this pass.

The native HCE example and public-text JVM tests pass offline. All four download files and
their URLs are unchanged. Chrome renders all nine pages at 360, 768 and 1440 CSS pixels in
light and dark modes (54 checks), without broken images or horizontal page overflow. Public
pages omit app release numbers, roadmap text and private source-tool names. Project records
and validation tools are excluded from the Pages build. The checks are local, not evidence
of a GitHub Pages deployment.

## HCE 1.0.0 final site review — 2026-11-13

The prepared HCE guide matches the 24-profile release catalog, its ordering and four in-app
guidance panels. Shortcut links make the two-tap workflow, history and JSON examples reachable
without scrolling through the entire guide. Stable example URLs, IDs and file contents remain
unchanged; all four are valid native HCE imports with envelope 1 / payload 3. The website
checker also verifies exactly one download action per public example. EMV retains its
independent guide/trace scope.

PASS: nine pages, 91 local references, four native downloads, three exact privacy mirrors,
and 20 checker tests. The browser renders all nine pages at 360, 768 and 1440 CSS pixels in
light and dark modes (54 checks), with no page-width overflow or broken images. The four
example URLs serve the expected JSON. Privacy wording and effective dates match the app
sources and remain unchanged. No source-tool names in public pages or downloads. Commit
locally only; push and publication remain separate.

## JCB final cleanup verification — 2026-11-09

PASS: 17 checker unit tests, including four isolated stable-download inventory checks for
complete/missing/extra/mislabelled examples. Static validation still covers 9 HTML pages,
83 references, 4 profile envelopes and 3 exact privacy mirrors. HCE native integration and
five-source JCB parity pass in the full module gate; the isolated instrumentation APK also
assembles. Existing responsive visual evidence remains applicable because no layout, CSS
or image changes occur in this cleanup. Prepare local commits only, without publication.

## JCB fourth-example verification — 2026-11-09

The native HCE importer accepts all four downloads under current payload 3 with distinct IDs. HCE integration replays JCB plain/requested-CDA first ARQC at low/high software inputs, changes the effective MK-AC, restores defaults and checks unchanged stored/security/APDU contracts plus selected PIN 1234. The published guidance targets the source-reviewed above-limit purchase, not newly claimed below-limit reader acceptance. Existing MC/Amex/Visa integration remains covered.

The static checker reports nine HTML pages, 83 local references, four profile envelopes/JSON illustrations and three exact policy body/date mirrors. Thirteen checker unit tests pass. Public downloads use CUSTOM-only provenance and contain no external source-tool name. Existing schema and policy dates stay unchanged. Local browser geometry at 1280 and 360 px shows all four cards in the existing 2×2 or single-column layout, without horizontal page overflow; desktop sample area is visually reviewed. Assets/CSS are unchanged. Nothing is pushed or deployed.

## Release-ready website and profile examples — 2026-11-09

Prepare the full local site for HCE 1.0.0, not as a development preview of the old production release. Guides describe the current 24-profile/43-scenario catalog, optional mapped simulated device verification, payload 3, compatibility 1/2, PIN policy, security/Reset and reader/host limits. EMV guide/trace reference matches its prepared bounded reader/privacy implementation and independent trace payload 2.

Replace all three downloads with current physical Visa Online PIN, Mastercard Online PIN and Amex Adaptive CVM definitions. Preserve stable download URLs, use distinct semantic web IDs, CUSTOM-only provenance, matching synthetic security/certificates and full structured guidance. Visa/MC request Online PIN even below the reader limit; Amex has an adaptive above-limit preference. Native integration verifies imports, payload 3, exact operational-contract parity, low/high APDUs, dynamic cryptograms, requested MC/Amex CDA, custom/default comparisons and selected-card PIN display. Old installed imports remain snapshots; old HCE versions may reject the new downloads. Publish only with the matching application release.

Review all policies against their app sources. HCE adds a test-only simulated-verification explanation (no biometric/unlock credentials), effective November 9, 2026; it retains local storage, no-backup profiles, temporary override, report/log/clipboard and deliberate-sharing boundaries. EMV wording/dates remain unchanged. The checker compares body and effective date for the policy mirrors and rejects external source labels in public HTML or complete JSON downloads. Internal maintenance/provenance records are not public UI copy.

PASS: nine HTML routes, eighty local references, three native downloads/JSON illustrations and three policy mirrors; thirteen parser/guidance/date/source-label regressions. Local responsive review at 1280×900 and 360×900: all nine pages have no horizontal page overflow or broken images; new wrapping sample cards/download actions are visually reviewed. Existing artwork, shared CSS, typography and navigation retain the established design. No remote upload, push or Pages publication occurs. Earlier payload-2/development-preview checkpoints below are historical and superseded for this prepared site.

Run `python3 tools/check_site.py` and `python3 -m unittest discover -s tools`; also run the sibling HCE native tests with `HCE_WEB_EXAMPLE_DIR` set. Browser checks use the local-only HTTP server. Deployment is a separately authorized push/Pages action.

## Amex development catalog alignment — 2026-11-09

Local-only guide/reference alignment with the HCE 24-profile / 43-scenario development catalog: seven refreshed American Express paths, payload 3, common PIN policy, optional mobile EMV two-presentation CVM, application-key/ICC Mixed and Reset semantics, and dynamic GET DATA ATC. Public downloadable examples remain envelope 1 / payload 2 for the published application; no new source data or private CA/issuer keys are published. This introduces no collection/network-processing change and no privacy-policy effective-date change. Validation passes for nine HTML pages, 80 local references, three native profile envelopes/JSON illustrations and three policy mirrors, plus four checker unit tests. The actual HCE importer also accepts the three unchanged published downloads. Existing graphics/styles remain unchanged; the text updates use the existing guide layout. Commit is authorized; push and GitHub Pages publication are not.

## Topics

- [Local final reviews](#README-local-final-reviews)
- [Verification history](#README-verification-history)
- [Repeatable offline validation](#repeatable-offline-validation)


<a id="README-local-final-reviews"></a>
## Local final reviews

<a id="README-verified-local-documentation-checkpoint--2026-10-25"></a>
### Verified local documentation checkpoint — 2026-10-25

The owner authorizes local checkpoint commits after HCE/EMV/Common cleanup. Review development
profile/history/explicit-control guidance while retaining the published-app boundary. Nine HTML
pages, eighty local references, three profile envelopes/policy mirrors and four checker tests
pass. Graphics, released downloads, privacy categories/effective dates and deployed content
remain unchanged. No push/deployment.

<a id="README-hce-development-target-promoted-to-100--2026-10-25"></a>
### HCE development target promoted to 1.0.0 — 2026-10-25

The owner renamed HCE's unreleased 0.2.0 target to 1.0.0 (16). This does not publish a release,
change profile/history schemas or expand scope. EMV keeps its own version target. Historical
review/build evidence below retains the original version labels; public guides stay version-free.
No commit, push or deployment.

<a id="README-explicit-emulator-controls--2026-10-25"></a>
### Explicit Emulator controls — 2026-10-25

Clarify that Change opens profile/security selection while metadata/card bodies remain inert;
simulated CVM uses its switch. Keep the existing workflow, styling and security/privacy limits.
The application upgrade is independently tested against the retained production schema-4 identity.
Local only; no commit, push or deployment.

<a id="README-remove-development-only-cvm-history-compatibility-align-phase-counts--2026-10-25"></a>
### Remove development-only CVM history compatibility; align phase counts — 2026-10-25

Discard old unpublished device-CVM records instead of converting them or retaining original-note
UI/export support. Released ordinary history and notes remain supported. Live/saved phase
headings share localized APDU counts. Local only; no commit, push or deployment.

<a id="README-one-durable-device-verification-scenario--2026-10-25"></a>
### One durable device-verification scenario — 2026-10-25

The HCE guide now describes one history record/note for both taps, a durable first checkpoint,
aligned overall live/list/detail outcomes and independently bounded APDU/check evidence in exports.
Recognizable old correlated groups preserve original notes; ambiguous records stay untouched.
Redacted omits all notes/identities/card-derived values. No native-profile/privacy-category change.
Local only; no commit, push or deployment.

<a id="README-locked-verification-inputs-and-first-tap-note-fallback--2026-10-25"></a>
### Locked verification inputs and first-tap note fallback — 2026-10-25

The HCE guide now keeps configuration locked while awaiting Continue and clarifies that Stop
before any second-tap APDU retains the first report and saved note, as Cancel does. No history,
JSON or privacy change. Local only; no commit, push or deployment.

<a id="README-empty-verification-attempts-and-terminal-notes--2026-10-25"></a>
### Empty verification attempts and terminal notes — 2026-10-25

Clarify that stopping before any APDU returns to the ordinary Emulation is off state, also
when leaving the tab/app. No note appears between taps; the saved presentation note follows
the final overview report before either APDU sequence. No schema/history/privacy change.
Local only; no commit, push or deployment.

<a id="README-classic-verification-status-and-terminal-report--2026-10-25"></a>
### Classic verification status and terminal report — 2026-10-25

Owner feedback supersedes the preceding progress/disclosure design. The HCE guide now keeps
the traditional animated waiting card through first tap, Continue and second tap. Only the
terminal state shows one conventional report with phase-labelled checks and both APDU sequences;
Cancel/expiry retains an interrupted first-tap report. No intermediate APDU/report UI, runtime
NFC rearming, schema change or combined history export is introduced. Local only; no deployment.

<a id="README-two-part-device-verification-summary--2026-10-25"></a>
### Two-part device-verification summary — 2026-10-25

The HCE development guide places Cancel/Continue in the normal Start/Stop area, outside Test
configuration. It describes stage progress, expandable first-tap evidence, the final two-part
live summary and partial cancellation/expiry, while keeping saved history/exports per presentation.
No key retention, real authentication, combined export or schema change is implied. Offline
site validation and all four checker tests pass. Local only; no commit, push or deployment.

<a id="README-simulated-verification-continuation--2026-10-24"></a>
### Simulated verification continuation — 2026-10-24

The HCE development guide now describes adjacent Cancel/Continue actions. Continue confirms
synthetic verification and arms tap two without another Start, only after field removal and
within the original two-minute window. Preserve profile/security binding, cancellation and
fresh terminal data; do not imply real wallet authentication. Offline site validation and all
four checker tests pass. No released JSON/download, privacy, commit, push or deployment change.

<a id="README-development-catalog-and-guidance-review--2026-10-25"></a>
### Development catalog and guidance review — 2026-10-25

The unpublished HCE guide now identifies the twenty-profile development catalog and thirty-five
Test guidance scenarios, including seven-for-four Visa and five-for-four Mastercard replacements, fixed versus adaptive CVM,
above-limit reader-policy limits and optional mobile two-presentation instructions. The JSON guide
keeps payload-3 development guidance separate from the released payload-2 downloads. Existing
downloads, production text/assets, privacy policies and deployment remain unchanged. Reference
PINs are not device-unlock codes; card-side checks are not host approval. The five Mastercard profiles
explain PIN-only below-limit reader support, terminal-CVM magstripe, mobile retry limits and Reset.
Only local checkpoint commits are authorized; no push/publication.

<a id="README-visa-refreshschema-preview-audit--2026-10-22"></a>
### Visa refresh/schema preview audit — 2026-10-22

The JSON guide distinguishes the current released payload 2/downloads from unpublished next-release
support for one consolidated payload 3: selected JCB scenarios plus optional response states,
personalized Visa CVN22 keys and adaptive CTQ. Released payload 1/2 remains readable. Document state guards, successful
transitions and activation reset without claiming persistent risk or a new payment engine. The six
new Visa conversions remain private staging candidates; no catalog, download, screenshot, privacy
policy or publication is changed. App guidance and the local technical documentation agree on the
same development-only boundary. Public site text/assets and downloadable JSON contain no external
reference-tool labels. Internal compatibility names in sibling projects are not public website copy.
The additional No-CVM candidate matches three captured source transactions; it is not advertised
as a released download or an accepted native-device profile. Its conversion needs no new schema.

<a id="README-form-factor-guidance-clarification--2026-10-22"></a>
### Form-factor guidance clarification — 2026-10-22

Clarify that physical/tokenized is an intended synthetic card scenario, separate from profile
origin, CVM results and the phone running HCE. A confirmed CVM result is not evidence of token
provisioning. Retain all three existing downloads and their payload schema 2; do not introduce
Reference or advertise unpublished JCB support. The HCE project records the complete local
sixteen-profile form-factor audit and the source-availability limits. Offline site validation,
all four checker tests and the real HCE importer check of all three downloads pass. Local only;
no commit, push or deployment.

<a id="README-history-presentation-follow-up--2026-10-18"></a>
### History presentation follow-up — 2026-10-18

The development guides now describe report-colored history list cards and neutral status/time
overviews above separate colored reports. HCE coloring follows saved profile checks, so a
negative scenario may still pass; EMV colors follow the analysis result. Labels remain explicit
and color is not proof of payment approval or card authenticity. Profile cards stay neutral.
Offline site validation and four checker tests pass. The owner authorized local commits only;
development notices remain and no push or deployment is performed. JCB HCE support stays
conditional at that checkpoint, pending further source and reader verification.

### EMV documentation check — 2026-11-17

The local developer guide describes bounded C-2–C-7 diagnostics, currently supported application
families, lifecycle and History workflows. The JSON reference uses envelope 1 and Full-only payload
2 and explains the schema 1 Full import alias and APDU source bounds. The privacy page matches
its application Markdown source. Offline checks pass for public copy, references, JSON and privacy.
All nine pages also pass layout checks in local Chrome at 360, 768 and 1440 CSS pixels in light
and dark modes, with four validated download links.

<a id="README-development-documentation-closeout--2026-10-16"></a>
### Development documentation closeout — 2026-10-16

Prepared locally for HCE/EMV 0.2.0 without push or publication. Guides now describe the compact
Emulator/Analyzer, separate profile/general guidance, neutral list cards and result badges,
mapped simulated device CVM and its two-presentation/security/lifecycle limits. At that checkpoint
EMV documentation described bounded C-2–C-7 reading and the trace format at that checkpoint.
The three downloadable synthetic HCE profiles were checked through the native HCE importer.
HCE JCB emulation remained conditional at this checkpoint.

The October preview used notices to distinguish draft documentation from the then-published apps.
The home page and existing stylesheet were unchanged.
The check compared the EMV privacy HTML to the application Markdown. The drafts kept the
published effective date pending release confirmation.

Run `python3 tools/check_site.py` and `python3 -m unittest discover -s tools` for offline checks.
The checker covers HTML headings/anchors, local links/assets, JSON illustrations, download
envelopes/unique IDs and privacy mirrors in the sibling application repositories. It performs
no network requests or deployment and does not replace the native-import test or browser review.

<a id="README-emv-publication-confirmation--2026-10-12"></a>
### EMV publication confirmation — 2026-10-12

The owner confirmed approval and production publication of EMV 0.1.4 (5). Samsung's production
Play package was verified at that version, with successful startup and saved History visible.
The owner subsequently confirmed the Pixel production update and retained History; both devices
show the production listing normally after resolving the stale Play display on Samsung.
Source development begins 0.2.0 (6), with its larger scope to be agreed separately. This does not
change public website copy, privacy practices, effective dates or interchange schemas. The
submission review below already verified the published sources against all public routes.
No additional website deployment is needed. Earlier pending statuses describe that review stage.

<a id="README-emv-production-submission-review--2026-10-12"></a>
### EMV production-submission review — 2026-10-12

The owner reports submitting the EMV service update with the production release and updated
full descriptions/screenshots in all six listing languages. This is submission evidence;
approval and publication of that update have not yet been confirmed.

Reviewed Home, the guide index, all three application guides, the JSON specification and all
three privacy policies. The EMV guide already covers retained live results, explicit NFC restart,
masked Summary, detailed Full evidence/Redacted exports and legacy payload-version import.
The importer and technical trace documentation agree with the schema reference. Each public
privacy body matches its application's Markdown after whitespace/markup normalization;
data practices and effective dates are unchanged.

All nine live HTML routes, the stylesheet, sitemap and three downloadable JSON profiles returned
HTTP 200 and matched local sources byte-for-byte. All 80 local links/assets and anchors pass;
public HTML contains no fixed application release numbers. Profile examples retain envelope
schema 1/payload schema 2; EMV trace payload remains schema 1. No public content correction,
new visual change or website deployment is needed for this submission review.

<a id="README-follow-up-review--2026-10-11"></a>
### Follow-up review — 2026-10-11

Reviewed the routes against the HCE, EMV and common project documentation,
privacy policies and importer implementation. Updated the home summary, added a
dedicated Copy workflow and provenance explanation, and documented exact profile
identity limits and conflicting EMV trace version aliases. Shared focus styling covers scrollable
code and tables, with one stylesheet cache revision across all pages. The light-theme
link token was slightly darkened so small accent text meets 4.5:1 contrast on the
shared muted surfaces as well as white backgrounds.

Verification: 80 local link/asset references, unique anchors, single H1 per page,
and all three download envelopes/payloads passed checks. All 23 tests in the HCE
BundledCardImageValidationTest suite passed without skips, including validation of
the actual website downloads and the Amex example session. All nine routes rendered
at 360, 768 and 1440 px in the browser's dark theme without page-width overflow or
missing images. Light-theme token contrast was reviewed separately; this follow-up
does not claim a new light-theme browser matrix. Policy body text matches each
project's Markdown after whitespace/markup normalization, so effective dates stay
unchanged. Store destinations and GitHub privacy reference were checked separately.

The downloads already represent valid, coherent synthetic fixtures and did not need
rewriting. Source documentation already describes the current security and schema
boundaries. No application code, collection practices or publication state changed.
These follow-up edits are retained locally; no push or deployment was performed.

<a id="README-previous-review-evidence--2026-10-10"></a>
### Previous review evidence — 2026-10-10

Prepared locally against current HCE/EMV/common behavior, without push or publication. HCE
guidance now describes confirmed Reset, Cancel/Apply, next-run versus active-session security
source and workspace retention; EMV guidance explains retention and the History → Import action.
Profile field editing and native profile export are not presented as available features.
Existing envelope/payload specifications and the three coherent synthetic examples stay intact;
all examples pass the actual HCE importer with payload schema 2.

All nine pages render at 360/768/1440 px in light/dark themes (54 combinations), with no broken
local links/anchors, missing images or page-width overflow. Visual checks retain shared typography,
spacing, cards, navigation and responsive tables/code blocks. Public pages contain no fixed application release
numbers. Privacy wording still matches local processing, explicit sharing and backup boundaries;
effective dates remain unchanged. Publication requires a separate owner decision.


<a id="README-verification-history"></a>
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
shared styles or availability links were changed. The site remains a local
draft; this review does not publish it.

Serve the root with `python3 -m http.server 8080 --bind 127.0.0.1` and open
`http://127.0.0.1:8080`. Check every page at desktop and phone widths in light and dark modes,
including navigation, focus states, readable tables, long code blocks, canonical URLs, image
loading, local links, privacy wording and sitemap entries. Verify that the in-app guidance URLs
match the guide routes here. Do not treat a local preview as public availability.

<a id="README-final-local-website-review--2026-10-01"></a>
### Final local website review — 2026-10-01

All HTML pages at that checkpoint were rendered in an isolated Chrome browser
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
documentation and History controls, shared format rules, and
in-app guide URLs. HCE guidance now explains APDU timing boundaries, deletion without erasing old
sessions, and repeating a session's Profile ID dependency. EMV guidance names report formats and
History filtering/Undo. Both guides caution that Redacted exports are not an anonymity guarantee.
The HTML policies were compared with their application's Markdown policy; dates remain draft
dates pending the separately authorized publication step. Update the effective date of revised
policy wording and its matching Markdown on publication, not merely on local review. Icon artwork,
store track destinations remain unchanged. No push or Pages deployment
was performed as part of this review.

## Repeatable offline validation

From the repository root run `python3 tools/check_site.py` and
`python3 -m unittest discover -s tools`. The checker validates routes/assets, unique headings
and anchors, JSON illustrations/download envelopes and sibling privacy mirrors without
network access or deployment. Native importer checks and browser accessibility/layout review
are separate gates. Never infer publication from a local successful check or commit.
