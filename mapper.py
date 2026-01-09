import argparse
import json
from pathlib import Path
from collections import defaultdict

from extractors.endpoints import extract_endpoints
from extractors.params import extract_parameters
from extractors.secrets import extract_secrets
from output.report import build_markdown_report, build_json_report
from utils.js_loader import load_js_sources


def map_attack_surface(targets):
    sources = load_js_sources(targets)
    results = {
        "endpoints": [],
        "parameters": [],
        "secrets": [],
        "metadata": {"total_sources": len(sources)},
    }

    for source in sources:
        content = source["content"]
        origin = source["origin"]
        endpoints = extract_endpoints(content, origin)
        params = extract_parameters(content, origin, endpoints)
        secrets = extract_secrets(content, origin)
        results["endpoints"].extend(endpoints)
        results["parameters"].extend(params)
        results["secrets"].extend(secrets)

    return results


def group_endpoints_by_domain(endpoints):
    grouped = defaultdict(list)
    for ep in endpoints:
        domain = ep.get("domain") or "unknown"
        grouped[domain].append(ep)
    return grouped


def main():
    parser = argparse.ArgumentParser(
        description="JavaScript attack surface mapper for bug bounty hunters"
    )
    parser.add_argument(
        "targets",
        nargs="+",
        help="Local JS paths (files or directories) or URLs to fetch",
    )
    parser.add_argument(
        "--json",
        dest="json_path",
        default="attack-surface.json",
        help="Where to write JSON output (default: attack-surface.json)",
    )
    parser.add_argument(
        "--md",
        dest="markdown_path",
        default="attack-surface.md",
        help="Where to write Markdown report (default: attack-surface.md)",
    )

    args = parser.parse_args()
    results = map_attack_surface(args.targets)

    markdown = build_markdown_report(
        endpoints=results["endpoints"],
        parameters=results["parameters"],
        secrets=results["secrets"],
    )
    json_output = build_json_report(results)

    Path(args.markdown_path).write_text(markdown, encoding="utf-8")
    Path(args.json_path).write_text(json.dumps(json_output, indent=2), encoding="utf-8")

    print(f"[+] Markdown report written to {args.markdown_path}")
    print(f"[+] JSON output written to {args.json_path}")


if __name__ == "__main__":
    main()

