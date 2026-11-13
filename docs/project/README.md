# HCEImage website project records

Planning, execution evidence and maintenance are separate from the technical specification.

## Navigation

- [Technical documentation](../README.md) — current contracts and specifications
- [Verification](verification.md) — procedures, audits, executed results and their limits
- [Maintenance](maintenance.md) — material decisions, changes and delivery history

## Documentation rules

Technical specifications describe the current checked-in implementation: contracts, schemas,
algorithms, supported behavior, ownership, limits and normative references. Link to relevant
source/tests where they explain a contract. Do not insert work progress, planned capabilities,
dated execution counts, device installations, benchmark results or release checkpoints there.
Technical pages link only to other technical pages and the documentation index, not to project
records, roadmaps or delivery checklists. The documentation index is the explicit boundary.

Project records may link to the technical contract they assess. Keep planned work in roadmap,
verification methods/results in verification, and consequential decisions/change/delivery history
in maintenance. Reuse these thematic documents rather than adding a file for each audit or task.
Do not create empty counterparts solely for symmetry. Common library specifications stay generic;
consumer-specific transports, application state and release workflows belong to their owner.

Use concise factual English, one sentence-case H1, descriptive H2/H3 sections, relative links and
blank lines around headings/lists/code. Preserve official names, API identifiers and protocol
acronyms. Schemas and limits are not application versions. Source-backed limits are part of a
contract; a dated unperformed/passed test is project evidence, not additional product behavior.

Update the existing technical topic when behavior changes. Record only material project outcomes,
with the date, exact scope, source/evidence identity and limitations. Avoid per-build/per-install
diaries and duplicate summaries. Preserve meaningful historical evidence and identify superseded
checkpoints as historical; Git retains previous wording. Never turn compilation, a synthetic
vector or a local card-side check into physical acceptance, host authorization or certification.

Keep raw licensed inputs, device logs, keys and machine-local backups outside public repositories.
Refer to retained evidence without copying sensitive or restricted source material into Markdown.
Private evidence identifiers are records, not required runtime inputs or public links.

After moves, validate files and anchors, verify the technical/project link boundary, preserve
cross-repository ownership and review changed paths. Documentation reorganization does not
authorize a code change, data deletion, commit, push, app installation or website deployment.
