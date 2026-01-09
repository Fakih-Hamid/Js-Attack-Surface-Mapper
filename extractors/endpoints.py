from urllib.parse import urlparse

from utils.patterns import (
    ENDPOINT_URL_REGEX,
    FETCH_CALL_REGEX,
    AXIOS_CALL_REGEX,
    XHR_OPEN_REGEX,
    GRAPHQL_HINT_REGEX,
    WEBSOCKET_REGEX,
)
from utils.patterns import finditer_unique


def normalize_endpoint(url):
    parsed = urlparse(url)
    domain = parsed.netloc or "unknown"
    path = parsed.path or "/"
    scheme = parsed.scheme or "http"
    return {
        "url": url,
        "domain": domain,
        "path": path,
        "scheme": scheme,
        "potential_impact": guess_impact(path),
    }


def guess_impact(path):
    path_lower = path.lower()
    if any(keyword in path_lower for keyword in ["admin", "internal", "private"]):
        return "auth-required"
    if any(keyword in path_lower for keyword in ["user", "account", "profile"]):
        return "idor-candidate"
    return "public"


def _extract_urls(content):
    urls = set()
    for match in ENDPOINT_URL_REGEX.finditer(content):
        urls.add(match.group(0))
    return urls


def _extract_calls(content):
    urls = set()
    for regex in [FETCH_CALL_REGEX, AXIOS_CALL_REGEX, XHR_OPEN_REGEX, WEBSOCKET_REGEX]:
        for match in regex.finditer(content):
            url = match.group(1)
            urls.add(url)
    return urls


def extract_endpoints(content, origin):
    urls = _extract_urls(content) | _extract_calls(content)
    endpoints = []
    for url in urls:
        endpoint = normalize_endpoint(url)
        endpoint["origin"] = origin
        endpoint["graphql"] = bool(GRAPHQL_HINT_REGEX.search(content))
        endpoints.append(endpoint)
    return endpoints

