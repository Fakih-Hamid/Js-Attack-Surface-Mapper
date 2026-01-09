# JS Attack Surface Mapper

Minimal Python utility to harvest offensive-relevant details from JavaScript for bug bounty and pentests.

## Why
- Quickly surface hidden endpoints, params, and secrets in bundled/minified JS.
- Produce Markdown for note-taking and JSON for automation.
- No heavyweight deps; ready for drop-in usage on targets or loot archives.

## Install
Python 3.8+; no external requirements.

```bash
python mapper.py --help
```

## Usage
Analyze local files, directories, or remote JS URLs:

```bash
python mapper.py ./public/js https://target.com/app.js
```

Outputs:
- `attack-surface.md`: human-readable report grouped by domain.
- `attack-surface.json`: structured data for your pipeline.

Change output locations:
```bash
python mapper.py ./dist --md recon.md --json recon.json
```

## Example
Use the included sample:

```bash
python mapper.py examples/sample.js --md sample-report.md --json sample-report.json
```

## What it extracts
- Endpoints: hardcoded URLs, fetch/axios/XHR/WebSocket calls, GraphQL hints.
- Parameters: query strings, inline body keys, fragments inside JS.
- Secrets: Authorization headers, JWTs, API keys, OAuth hints, generic tokens.

## Extending
- Add regex/patterns in `utils/patterns.py`.
- Enhance collectors in `extractors/` (endpoints, params, secrets).
- Adjust reporting in `output/report.py`.

## Notes
- Treat findings as leads; confirm with requests and proper scoping.
- Consider piping JSON into your own active probes (SSRF, IDOR, auth bypass).

