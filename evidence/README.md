# Evidence Archive

This directory tracks localized source evidence used to validate potential collaboration opportunities.

## What Is Committed

- `evidence/index.yml` is the durable manifest of localized source URLs.
- `evidence/notes/` stores lightweight Markdown evidence notes for agent review.
- `evidence/raw/.gitkeep` and `evidence/reports/.gitkeep` preserve ignored working directories.

## What Is Ignored

- `evidence/raw/` stores fetched raw HTML, PDF, text, and extracted Markdown captures.
- `evidence/reports/` stores generated pass reports from localization runs.

Raw captures are ignored by default because webpages can be copyrighted, bulky, or operationally noisy. The committed notes and manifest are the stable audit layer; raw local files are reusable within the working copy when present.

## Workflow

Use `scripts/localize_evidence.py` before importing completed research into chapter opportunity front matter.

Typical usage:

```bash
python3 scripts/localize_evidence.py --from research/completed/example.md
python3 scripts/localize_evidence.py --from chapters/north-america/sacramento/index.md
python3 scripts/localize_evidence.py --url https://example.org/source-page
```

The script:

- extracts URLs from reports, chapter pages, or explicit `--url` arguments;
- skips URLs already listed in `evidence/index.yml` when the note and raw Markdown paths still exist;
- fetches missing URLs and saves raw captures under `evidence/raw/`;
- writes Markdown evidence notes under `evidence/notes/`;
- updates `evidence/index.yml`;
- writes pass reports under ignored `evidence/reports/`;
- prints a concise summary showing localized, skipped, and failed URLs with evidence paths.

Use `--refresh` when a source should be fetched again even if it was already localized. Use `--dry-run` to see what would happen without fetching or writing files.

## Validation Standard

Future integration passes should consult local evidence notes first. If a URL is already localized and the note/raw paths exist, use those files for source review before re-fetching the website. Re-fetch only when local evidence is missing, stale, incomplete, or disputed.
