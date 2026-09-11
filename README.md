# HCEImage website

Public website, support and privacy information for HCEImage applications. Static HTML and CSS
are served by GitHub Pages; there is no application backend, analytics or build dependency.

## Content

- [Home](index.html) — application descriptions and current availability.
- [HCE Test Tool privacy policy](hce-test-tool/privacy-policy/index.html) — local history,
  notes, reports, clipboard, diagnostic logs, NFC, Android backup and support contact.
- [EMV Card Analyzer privacy policy](emv-card-analyzer/privacy-policy/index.html) — current
  0.1.0 build with local contactless reading, persistent history, notes and explicit report export.
- [ECR Test Tool privacy policy](ecr-test-tool/privacy-policy/index.html) — current 0.1.0
  development foundation; live ECR-B communication, transaction history and reports remain planned.
- [Shared styles](assets/styles.css) — responsive layouts and light/dark appearance.
- [Sitemap](sitemap.xml) — public canonical pages.

## Availability

HCE Test Tool 0.1.11 (11) is published in open testing as of September 11, 2026.
The developer verified tester enrollment, Google Play update delivery and startup on Pixel and
Samsung, quick functional checks, and discovery through Google Play search.
The home page links to [Join the test](https://play.google.com/apps/testing/com.hceimage.hcetesttool).
EMV Card Analyzer 0.1.0 (1) was published to internal testing on September 11, 2026. Tester
enrollment, Google Play installation and application startup were confirmed. ECR Test Tool remains
in development. All privacy links use the same

presentation and align horizontally on desktop; mobile actions align left with the card content.

## Maintenance

Keep public descriptions aligned with implemented features and clearly label planned functionality.
Synchronize each policy's wording and effective date with its application repository's
`play/privacy-policy.md`. Website SVG icons mirror each application's `play/assets/icon-source.svg`.
The website uses a tighter `16 16 76 76` viewBox for readability at small sizes; paths, gradients
and transforms remain identical. CSS supplies rounded presentation corners.

Privacy wording was reviewed on September 7, 2026 against application data flows and the
[Google Play User Data guidance](https://support.google.com/googleplay/android-developer/answer/10144311)
and [GitHub Pages hosting behavior](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages).
Recheck it whenever data handling changes.

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
policy wording for local history, notes, retention and report export. After the first release was
confirmed, the home page status was updated to Internal testing.

The September 11, 2026 dark-mode compatibility update declares light and dark support in every
page before styles load and marks application icons as light-only surfaces. The home page serves
512 px PNG renditions of the SVG source artwork because Samsung Internet applies an unavoidable
forced-dark color transformation to small SVG images. The raster renditions preserve the intended
light icon surfaces in that browser. The primary action uses dedicated light and dark colors so it
retains sufficient contrast after Samsung Internet applies its forced-dark transformation.
