import re
from urllib.parse import urlparse


ENDPOINT_URL_REGEX = re.compile(
    r"(https?://[^\s\"'<>]+|wss?://[^\s\"'<>]+)", re.IGNORECASE
)

FETCH_CALL_REGEX = re.compile(r"fetch\(\s*['\"]([^'\"]+)['\"]", re.IGNORECASE)
AXIOS_CALL_REGEX = re.compile(r"axios\.(get|post|put|delete|patch)\(\s*['\"]([^'\"]+)['\"]", re.IGNORECASE)
XHR_OPEN_REGEX = re.compile(r"\.open\(\s*['\"][A-Z]+['\"]\s*,\s*['\"]([^'\"]+)['\"]", re.IGNORECASE)
WEBSOCKET_REGEX = re.compile(r"new\s+WebSocket\(\s*['\"]([^'\"]+)['\"]", re.IGNORECASE)

GRAPHQL_HINT_REGEX = re.compile(r"graphql|gql|\/graphql", re.IGNORECASE)

QUERY_PARAM_REGEX = re.compile(r"([a-zA-Z0-9_\-]+)=([a-zA-Z0-9_\-]+)")
BODY_KEY_REGEX = re.compile(r"[\"']([a-zA-Z0-9_\-]{3,})[\"']\s*:\s*")

AUTH_HEADER_REGEX = re.compile(r"Authorization\s*:\s*[\"']?Bearer\s+[A-Za-z0-9\-_=\.]+", re.IGNORECASE)
JWT_REGEX = re.compile(r"[A-Za-z0-9\-_=]+\.[A-Za-z0-9\-_=]+\.([A-Za-z0-9\-_.+/=]+)?")
API_KEY_REGEX = re.compile(r"(?:api[_-]?key|x-api-key)[\"']?\s*[:=]\s*[\"']([A-Za-z0-9\-_]{16,})", re.IGNORECASE)
OAUTH_HINT_REGEX = re.compile(r"(client_secret|client_id|refresh_token)", re.IGNORECASE)
GENERIC_SECRET_REGEX = re.compile(r"(?:secret|token|key)[\"']?\s*[:=]\s*[\"']([A-Za-z0-9\-_]{12,})", re.IGNORECASE)


def finditer_unique(regex, content):
    seen = set()
    for match in regex.finditer(content):
        value = match.group(0)
        if value in seen:
            continue
        seen.add(value)
        yield match

