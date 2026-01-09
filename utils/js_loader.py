import glob
from pathlib import Path
from urllib.parse import urlparse
import urllib.request


def _read_file(path):
    p = Path(path)
    if p.is_dir():
        contents = []
        for js_file in p.rglob("*.js"):
            contents.append({"origin": str(js_file), "content": js_file.read_text(encoding="utf-8", errors="ignore")})
        return contents
    return [{"origin": str(p), "content": p.read_text(encoding="utf-8", errors="ignore")}]


def _download_url(url):
    with urllib.request.urlopen(url) as resp:
        body = resp.read().decode("utf-8", errors="ignore")
    return {"origin": url, "content": body}


def load_js_sources(targets):
    sources = []
    for target in targets:
        if target.startswith("http://") or target.startswith("https://"):
            sources.append(_download_url(target))
        else:
            sources.extend(_read_file(target))
    return sources

