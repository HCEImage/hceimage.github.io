# HCEImage website

Public website, support and privacy information for HCEImage applications. Static HTML and CSS
are served by GitHub Pages; there is no application backend, analytics or build dependency.

## Content

- [Home](index.html) — application descriptions and current availability.
- [Developer guides](guides/index.html) — public application guidance, separated into
  HCE Test Tool and EMV Card Analyzer sections.
- [HCE Test Tool guide](guides/hce-test-tool/index.html) — controlled card-profile emulation,
  APDU inspection, validation, history, reports and optional test-security overrides.
- [EMV Card Analyzer guide](guides/emv-card-analyzer/index.html) — bounded contactless analysis,
  result states, APDU inspection, history and reports.
- [HCE Test Tool privacy policy](hce-test-tool/privacy-policy/index.html) — local history,
  notes, reports, clipboard, diagnostic logs, NFC, Android backup and support contact.
- [EMV Card Analyzer privacy policy](emv-card-analyzer/privacy-policy/index.html) — current Android
  application with local contactless reading, persistent history, notes and explicit report export.
- [ECR Test Tool privacy policy](ecr-test-tool/privacy-policy/index.html) — current 0.1.0
  development build with V5/V4 TCP profiles and a built-in Local POI; persistent history and reports remain planned.
- [Shared styles](assets/styles.css) — responsive layouts and light/dark appearance.
- [Sitemap](sitemap.xml) — public canonical pages.

## Availability

HCE Test Tool 0.1.12 (13) remains available as an Android application in open testing. The same
Play-accepted bundle, its updated en-US listing and its 177-country production configuration are
now under Google Play production review. Production availability has not yet been confirmed. The
application supports synthetic EMV contactless card profiles, optional in-memory test-security
overrides, structured APDU inspection, flow validation, local history, notes and user-initiated
diagnostic report export. The developer previously verified tester enrollment, Google Play update
delivery and startup on Pixel and Samsung, quick functional checks, and discovery through Google
Play search. Release-specific publication and post-publication verification are tracked in the
application repository. Until production availability is confirmed, the home page labels the review
state and links to [Join the open test](https://play.google.com/apps/testing/com.hceimage.hcetesttool).
EMV Card Analyzer 0.1.1 (2) is currently available as an Android application in open testing. Google Play
confirmed and published the signed update, refreshed store listing and current phone screenshots on September 15,
2026; the internal and closed tracks remain paused. Public enrollment, exact 0.1.1 Play delivery,
installation, startup and an authorized test-card analysis are confirmed. The home page links to
[Join the Android test](https://play.google.com/apps/testing/com.hceimage.emvcardanalyzer).
ECR Test Tool remains in development. Its current Android and desktop build supports nexo Retailer V5 and V4
over TCP, direct terminal connections, and an optional Local POI Sale simulation. Persistent history, full CASP-family
execution and reports remain planned. All privacy links use
the same presentation and align horizontally on desktop; mobile actions align left with the card content.

## Maintenance

Keep public descriptions aligned with implemented features and clearly label planned functionality.
Synchronize each policy's wording and effective date with its application repository's
`play/privacy-policy.md`. Website SVG icons mirror each application's `play/assets/icon-source.svg`.
The website uses a tighter `16 16 76 76` viewBox for readability at small sizes; paths, gradients
and transforms remain identical. CSS supplies rounded presentation corners.

Privacy wording was reviewed on September 15, 2026 against application data flows and the
[Google Play User Data guidance](https://support.google.com/googleplay/android-developer/answer/10144311)
and [GitHub Pages hosting behavior](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages).
Recheck it whenever data handling changes.

The HCE Test Tool policy was reviewed again during production preparation on September 22, 2026.
The production promotion and store-listing refinements do not change collection, storage, backup,
clipboard, logging, report sharing, NFC or support-email behavior. The September 15 effective date,
public wording and stable `/hce-test-tool/privacy-policy/` URL therefore remain unchanged.

## Local verification

Serve the repository root with `python3 -m http.server 8080 --bind 127.0.0.1` and open
`http://127.0.0.1:8080`. Check home and all three policies at desktop and mobile widths in both
color schemes, navigation, asset paths, canonical URLs and sitemap entries. Local commits do
not update the public site until they are pushed and the GitHub Pages deployment succeeds.

The September 7, 2026 review checked all three pages at mobile and desktop widths in light and
dark themes (12 browser views), with valid local links, loaded resources and no horizontal overflow.
Policy sections match their application Markdown sources; icon artwork matches the distribution SVGs.

The September 9, 2026 live-site review verified all three pages at mobile (390 px) and desktop
(1440 px) widths in light and dark themes. Page resources and internal navigation passed with
no horizontal overflow or browser errors. Public home HTML and CSS matched the repository;
the Applications section padding was 48 px on mobile and 72 px on desktop. The stylesheet is
served with a ten-minute cache lifetime, so an existing browser tab may need a forced reload.

The September 11, 2026 preparation updates the EMV Card Analyzer application card and publishes
policy wording for local history, notes, retention and report export. After the internal release was
confirmed and the closed release was published, the home page status was updated to Closed testing.

The September 11, 2026 dark-mode compatibility update declares light and dark support in every
page before styles load and marks application icons as light-only surfaces. The home page serves
512 px PNG renditions of the SVG source artwork because Samsung Internet applies an unavoidable
forced-dark color transformation to small SVG images. The raster renditions preserve the intended
light icon surfaces in that browser. The primary action uses dedicated light and dark colors so it
retains sufficient contrast after Samsung Internet applies its forced-dark transformation.

The September 13, 2026 ECR update replaces the obsolete ECR-B placeholder with the implemented nexo Retailer V5
and V4 profiles, TCP connection behavior, Local POI Sale simulation and current volatile-data boundary.

The September 14, 2026 availability update identifies HCE Test Tool and EMV Card Analyzer as Android applications
and labels their Google Play actions as Android open-test enrollment. ECR Test Tool remains identified as a
multiplatform Android and desktop application. Application data handling did not change, so the privacy policies remain unchanged.

The September 15, 2026 HCE Test Tool update refreshes its evergreen application summary. Its privacy
policy now distinguishes optional Test security data, which remains in memory, from generated synthetic
APDU results handled through the existing history, diagnostics, clipboard and report flows. EMV Card
Analyzer and ECR Test Tool content is unchanged.

The September 15, 2026 EMV Card Analyzer update makes the public policy version-independent
and refreshes the home-page summary around transport-neutral EMV inspection, contextual decoding, explicit result
states, offline references, local history and reports. The underlying data practices remain unchanged.

The September 15, 2026 publication record confirms EMV Card Analyzer 0.1.1 (2), its updated en-US
listing and eight refreshed screenshots in Google Play open testing. No visible website or privacy-policy
change was required because the public pages already described the released behavior.

The September 22, 2026 HCE Test Tool production update records submission of the existing 0.1.12
bundle, its updated en-US listing and its 177-country configuration for Google Play production
review. The home page identifies the pending review while retaining the working open-test enrollment
action. After Google Play confirms production availability, replace that action with the production
store listing and change the status to Android availability on Google Play. The developer guide,
privacy-policy URL and policy wording remain valid.
