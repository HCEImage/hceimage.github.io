# HCEImage website

Static GitHub Pages sources for application pages, developer guides, privacy policies and
synthetic downloadable examples. There is no backend, analytics or build dependency.

## Navigation

- [Documentation](docs/README.md) — site structure and content contract
- [Project records](docs/project/README.md) — validation, maintenance and deployment procedure
- [Home](index.html) — website entry point

## Local checks

```shell
python3 tools/check_site.py
python3 -m unittest discover -s tools
```

Local edits, checks and commits do not publish the site. Publication requires separate
authorization, a push and a successful GitHub Pages deployment.
