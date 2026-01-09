from collections import defaultdict
from urllib.parse import urlparse


def build_markdown_report(endpoints, parameters, secrets):
    md = []
    md.append("# JS Attack Surface Map\n")

    domains = defaultdict(list)
    for ep in endpoints:
        domains[ep.get("domain", "unknown")].append(ep)

    md.append("## Endpoints by domain\n")
    for domain, eps in domains.items():
        md.append(f"### {domain}")
        for ep in sorted(eps, key=lambda e: e.get("path", "")):
            impact = ep.get("potential_impact", "unknown")
            graphql = " (GraphQL)" if ep.get("graphql") else ""
            md.append(f"- `{ep['url']}` [{impact}]{graphql} (src: {ep['origin']})")
        md.append("")

    md.append("## Parameters\n")
    for param in parameters:
        loc = param.get("location", "unknown")
        endpoint = param.get("endpoint") or "n/a"
        md.append(f"- `{param['name']}`={param.get('value','')} ({loc}) -> {endpoint} (src: {param['origin']})")
    md.append("")

    md.append("## Secrets & tokens\n")
    for sec in secrets:
        md.append(f"- [{sec['type']}] `{sec['value']}` (src: {sec['origin']})")

    return "\n".join(md)


def build_json_report(results):
    return results

