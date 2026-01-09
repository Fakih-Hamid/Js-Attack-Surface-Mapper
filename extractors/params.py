from urllib.parse import urlparse, parse_qsl
import json

from utils.patterns import BODY_KEY_REGEX, QUERY_PARAM_REGEX


def _params_from_url(url):
    parsed = urlparse(url)
    params = []
    for key, value in parse_qsl(parsed.query):
        params.append(
            {
                "name": key,
                "value": value,
                "location": "query",
                "endpoint": url,
            }
        )
    return params


def _params_from_body_snippets(content):
    params = []
    for match in BODY_KEY_REGEX.finditer(content):
        key = match.group(1)
        params.append({"name": key, "location": "body", "endpoint": None})
    return params


def extract_parameters(content, origin, endpoints):
    found = []
    for ep in endpoints:
        found.extend(_params_from_url(ep["url"]))
    found.extend(_params_from_body_snippets(content))

    # Capture query-style patterns even when not full URLs
    for match in QUERY_PARAM_REGEX.finditer(content):
        found.append(
            {
                "name": match.group(1),
                "value": match.group(2),
                "location": "query-fragment",
                "endpoint": None,
            }
        )

    for item in found:
        item["origin"] = origin
    return found

