from utils.patterns import (
    JWT_REGEX,
    AUTH_HEADER_REGEX,
    API_KEY_REGEX,
    OAUTH_HINT_REGEX,
    GENERIC_SECRET_REGEX,
)
from utils.patterns import finditer_unique


def extract_secrets(content, origin):
    secrets = []
    for regex, kind in [
        (JWT_REGEX, "jwt"),
        (AUTH_HEADER_REGEX, "authorization-header"),
        (API_KEY_REGEX, "api-key"),
        (OAUTH_HINT_REGEX, "oauth"),
        (GENERIC_SECRET_REGEX, "secret"),
    ]:
        for match in finditer_unique(regex, content):
            secrets.append(
                {
                    "type": kind,
                    "value": match.group(0),
                    "origin": origin,
                }
            )
    return secrets

