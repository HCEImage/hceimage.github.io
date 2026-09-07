# HCEImage website

Public website, support and privacy information for HCEImage applications. Static HTML and CSS
are served by GitHub Pages; there is no application backend, analytics or build dependency.

## Content

- [Home](index.html) — application descriptions and current availability.
- [HCE Test Tool privacy policy](hce-test-tool/privacy-policy/index.html) — local history,
  notes, reports, clipboard, diagnostic logs, NFC, Android backup and support contact.
- [EMV Card Analyzer privacy policy](emv-card-analyzer/privacy-policy/index.html) — current
  0.1.0 foundation; card reading and saved analysis are not implemented yet.
- [Shared styles](assets/styles.css) — responsive layouts and light/dark appearance.
- [Sitemap](sitemap.xml) — public canonical pages.

## Maintenance

Keep public descriptions aligned with implemented features and clearly label planned functionality.
Synchronize each policy's wording and effective date with its application repository's
`play/privacy-policy.md`. Website SVG icons mirror each application's `play/assets/icon-source.svg`;
The website uses a tighter `16 16 76 76` viewBox for readability at small sizes; paths, gradients
and transforms remain identical. CSS supplies rounded presentation corners.

Privacy wording was reviewed on September 7, 2026 against application data flows and the
[Google Play User Data guidance](https://support.google.com/googleplay/android-developer/answer/10144311)
and [GitHub Pages hosting behavior](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages).
Recheck it whenever data handling changes.

## Local verification

Serve the repository root with `python3 -m http.server 8080 --bind 127.0.0.1` and open
`http://127.0.0.1:8080`. Check home and both policies at desktop and mobile widths in both
color schemes, navigation, asset paths, canonical URLs and sitemap entries. Local commits do
not update the public site until they are pushed and the GitHub Pages deployment succeeds.

The September 7, 2026 review checked all three pages at mobile and desktop widths in light and
dark themes (12 browser views), with valid local links, loaded resources and no horizontal overflow.
Policy sections match their application Markdown sources; icon artwork matches the distribution SVGs.
