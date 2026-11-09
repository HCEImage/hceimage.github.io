# HCEImage website maintenance

Material engineering decisions and delivery history. Older records retain the scope and
publication status at their recorded date; they are not current runtime documentation.


<a id="README-current-publication-status"></a>
## Amex development catalog alignment — 2026-11-09

Local-only guide/reference alignment with the HCE 24-profile / 43-scenario development catalog: seven refreshed American Express paths, payload 3, common PIN policy, optional mobile EMV two-presentation CVM, application-key/ICC Mixed and Reset semantics, and dynamic GET DATA ATC. Public downloadable examples remain envelope 1 / payload 2 for the published application; no new source data or private CA/issuer keys are published. This introduces no collection/network-processing change and no privacy-policy effective-date change. Validation passes for nine HTML pages, 80 local references, three native profile envelopes/JSON illustrations and three policy mirrors, plus four checker unit tests. The actual HCE importer also accepts the three unchanged published downloads. Existing graphics/styles remain unchanged; the text updates use the existing guide layout. Commit is authorized; push and GitHub Pages publication are not.

## Current publication status

On 2026-10-11 the owner confirmed HCE 0.1.14 (15) production publication and authorized
publication of the matching website follow-up. The six full descriptions and screenshot
sets accompany that release; image 4 shows Import while the APDU timeline and parsed
response remain included. This confirmation does not establish a device-level in-place
upgrade preservation test. The owner subsequently reported successful Samsung and Pixel updates
with history retained; other preserved data was not individually confirmed.

<a id="README-deployment-verification--2026-10-11"></a>
### Deployment verification — 2026-10-11

Published the prepared website through `main`. GitHub Pages successfully deployed content commit
`9bcc765887e6688562ac201ecabdce35cb1d87a0` in
[run 38158082373](https://github.com/HCEImage/hceimage.github.io/actions/runs/38158082373).
All nine public HTML routes, the shared stylesheet and all three downloadable JSON profiles
returned HTTP 200 and matched the prepared local sources byte-for-byte. This includes the
developer guides, privacy policies and envelope-1/profile-payload-2 synthetic examples.
Earlier local-only statements below describe preparation before this authorized publication.


<a id="README-previous-local-preparation-status"></a>
## Previous local preparation status

Local closeout on 2026-10-10 includes developer guides, privacy wording and the three downloadable
examples. All nine HTML pages passed internal link, anchor and asset validation; example envelopes
remain schema 1 and card-profile payloads schema 2. Changes are committed locally only: no push
or GitHub Pages publication is authorized for this closeout.

Local security/schema follow-up: the card-profile reference and three downloads now use payload
schema 2 inside envelope schema 1. The reference explains generated legacy per-card keys, optional
KCV checking, fixed-result overrides, and the distinction from application cryptogram master keys.
EMV trace payload schema remains 1. These changes are prepared locally and are not yet published.
The HCE guide also reflects Copy/Created provenance and the private persistence boundary; its
local privacy page is aligned with the project policy, including legacy keys and excluding
temporary overrides from profile copies. No new collection or network processing is introduced.
Local verification: all nine HTML pages and internal links/anchors/assets passed, with no page
overflow in desktop and mobile browser checks. The three schema-2 downloads passed the actual
HCE native importer, including the Amex APDU/session check. The new reference section was visually
reviewed at desktop/mobile widths. Publication remains a separate, explicitly authorized step.

The owner confirmed HCE Test Tool approval and production publication on 2026-10-01. Its native
profile-import functionality, updated listing and screenshots are released. The previously
published guides and policies accompany that release. The follow-up website update adds visible
format-specification entry points and three downloadable, validated synthetic profile examples.
No app release numbers appear in public website copy. EMV production publication was confirmed on 2026-10-06; ECR has no
store action and its retained guide/policy routes remain absent from navigation and sitemap.

Production publication does not establish that an existing device has received its in-place
Play update; that preservation check remains tracked in the HCE release documentation.


<a id="README-publication-procedure"></a>
## Publication procedure

The site describes the prepared application functionality. Before publication, check the
matching application artifacts, Play listing, availability links and policy declarations. For the
coordinated HCE update, prepare the store listing, signed bundle and matching web documentation
together. The owner has now confirmed production publication and separately authorized this
website update. Future website publication must not be inferred from Console submission. A prepared
Console release is not a publicly available update. Editing or committing this repository does not
publish the site; publishing requires a separate push and successful GitHub Pages deployment.

The published HCE Play description and screenshots include native profile import and distinguish
persistent imported-profile defaults from the default one-use Emulator override and the optional
keep-until-app-close choice. Record application publication only with actual confirmation from
the owner or Play Console, not merely because store assets or a bundle have been saved.

The HCE and EMV Google Play links point to their production listings. ECR has no store action. The application cards identify supported platforms rather
than embedding app release numbers or treating distribution tracks as product capabilities.


<a id="README-privacy-and-effective-dates"></a>
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


<a id="README-publication-preparation--2026-10-01"></a>
## Publication preparation — 2026-10-01

The owner authorized publication after completing the local website review and preparing the HCE
listing, screenshots, release notes and signed bundle in Play Console. Updated guides and privacy
pages are published independently of the application review. HCE's Play update is still pending;
website publication does not establish that the new application is available on Google Play.
All revised policies use the publication date in both HTML and their application Markdown copies.
The retained ECR pages remain omitted from navigation and sitemap. Confirm live page content after
the Pages deployment before submitting the Console changes for review.


<a id="README-production-follow-up--2026-10-01"></a>
## Production follow-up — 2026-10-01

The owner confirmed application approval/publication and authorized this follow-up website
deployment. All nine pages passed another 54-render check at 360/768/1440 pixels in light/dark
modes, with no broken internal links, missing images, page overflow or browser errors. The example
cards were visually inspected in desktop light and phone dark layouts. Actual browser downloads
return the three expected `.hceimage.json` filenames and match the reviewed local bytes. All three
files pass native import, duplicate-ID/KCV rejection and complete engine/session validation.
Privacy text and dates match all three application Markdown copies. No policy wording change was
needed for the public synthetic examples; hosting remains separate from application processing.


<a id="README-emv-publication-follow-up--2026-10-05"></a>
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
ECR routes remain absent from navigation and sitemap. The follow-up was pushed to GitHub Pages and the two changed guides were fetched from the
public site after deployment; both match the committed HTML byte for byte. The other twelve
reviewed public files also match their repository copies. Website deployment is complete and
remains separate from the pending application Play-upgrade verification.


<a id="README-emv-production-availability--2026-10-06"></a>
## EMV production availability — 2026-10-06

The owner confirmed approval and production publication, including the six store-listing
languages. Home and the EMV guide now link to the production Google Play listing and use the
same Get it on Google Play action as HCE. Public pages remain free of application release numbers.
Privacy wording, effective dates, guides, JSON structures, artwork and shared styling otherwise
remain unchanged. Store translations do not imply translated application or website interfaces.
The owner confirmed that open testing was paused on 2026-10-06. Production remains active;
this track-status confirmation requires no further public-page change.

## Documentation structure — 2026-10-25

Separate current technical contracts from project scope, acceptance evidence and delivery
history. Consolidate overlapping audit files under `docs/project`, fold UI resource ownership
into the current UI specification and keep a documentation index as the navigation boundary.
Store files remain submission inputs; public website content and runtime code are unchanged.
Retained source records and performance JSON are preserved; existing unrelated workspace changes
are not reverted. This reorganization does not publish, install or commit any project.
