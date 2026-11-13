# HCEImage website

Static GitHub Pages sources for application pages, developer guides, privacy policies and
synthetic downloadable examples. There is no backend, analytics or build dependency.

## Local checks

```shell
python3 tools/check_site.py
python3 -m unittest discover -s tools
```

Local edits, checks and commits do not publish the site. Publication requires separate
authorization, a push and a successful GitHub Pages deployment.

## Documentation

- [Technical documentation](docs/README.md) — current contracts and feature specifications
- [Project records](docs/project/README.md) — scope, execution evidence and maintenance
- [Home](index.html) — website entry point

Technical pages do not carry roadmap status or dated test results. Project records refer to
the contracts they assess; publication and release acceptance are tracked separately.
