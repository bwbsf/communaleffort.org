#!/usr/bin/env python3
"""Localize source URLs into an evidence archive.

The script intentionally uses only the Python standard library so agents can run
it in constrained environments. Raw captures and generated reports are ignored by
git; the manifest and lightweight notes are committed governance artifacts.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import html
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import shutil
import sys
import textwrap
from typing import Iterable
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen


REPO_ROOT = Path(__file__).resolve().parents[1]
EVIDENCE_ROOT = REPO_ROOT / "evidence"
MANIFEST_PATH = EVIDENCE_ROOT / "index.yml"
NOTES_DIR = EVIDENCE_ROOT / "notes"
RAW_DIR = EVIDENCE_ROOT / "raw"
REPORTS_DIR = EVIDENCE_ROOT / "reports"
DEFAULT_TIMEOUT_SECONDS = 20


class MarkdownExtractor(HTMLParser):
    """Small HTML-to-Markdown-ish text extractor for source review."""

    BLOCK_TAGS = {
        "address",
        "article",
        "aside",
        "blockquote",
        "br",
        "dd",
        "div",
        "dl",
        "dt",
        "figcaption",
        "figure",
        "footer",
        "form",
        "h1",
        "h2",
        "h3",
        "h4",
        "h5",
        "h6",
        "header",
        "hr",
        "li",
        "main",
        "nav",
        "ol",
        "p",
        "pre",
        "section",
        "table",
        "tbody",
        "td",
        "tfoot",
        "th",
        "thead",
        "tr",
        "ul",
    }

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []
        self.skip_depth = 0
        self.current_href = ""

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        tag = tag.lower()
        if tag in {"script", "style", "noscript", "svg"}:
            self.skip_depth += 1
            return
        if self.skip_depth:
            return
        if tag in self.BLOCK_TAGS:
            self.parts.append("\n")
        if tag in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            level = int(tag[1])
            self.parts.append("\n" + "#" * min(level, 6) + " ")
        if tag == "li":
            self.parts.append("\n- ")
        if tag == "a":
            attrs_dict = {name.lower(): value or "" for name, value in attrs}
            self.current_href = attrs_dict.get("href", "")

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if tag in {"script", "style", "noscript", "svg"} and self.skip_depth:
            self.skip_depth -= 1
            return
        if self.skip_depth:
            return
        if tag == "a":
            self.current_href = ""
        if tag in self.BLOCK_TAGS:
            self.parts.append("\n")

    def handle_data(self, data: str) -> None:
        if self.skip_depth:
            return
        text = " ".join(data.split())
        if not text:
            return
        self.parts.append(text)
        if self.current_href and self.current_href.startswith(("http://", "https://")):
            self.parts.append(f" ({self.current_href})")
        self.parts.append(" ")

    def markdown(self) -> str:
        text = html.unescape("".join(self.parts))
        text = re.sub(r"[ \t]+\n", "\n", text)
        text = re.sub(r"\n{3,}", "\n\n", text)
        return text.strip() + "\n" if text.strip() else ""


def quote_yaml(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def utc_now() -> dt.datetime:
    return dt.datetime.now(dt.UTC)


def today() -> str:
    return utc_now().strftime("%Y-%m-%d")


def timestamp() -> str:
    return utc_now().strftime("%Y-%m-%d-%H-%M-%S")


def url_hash(url: str) -> str:
    return hashlib.sha256(url.encode("utf-8")).hexdigest()[:16]


def safe_hostname(url: str) -> str:
    host = urlparse(url).netloc.lower().split("@")[-1].split(":")[0]
    host = re.sub(r"[^a-z0-9.-]+", "-", host).strip(".-")
    return host or "unknown-host"


def normalize_url(raw_url: str) -> str:
    raw_url = raw_url.strip().strip("'\"").rstrip(".,;")
    markdown_link = re.match(r"\[(https?://[^\]]+)\]\((https?://[^)]+)\)", raw_url)
    if markdown_link:
        return markdown_link.group(2).strip()
    if raw_url.startswith("<") and raw_url.endswith(">"):
        raw_url = raw_url[1:-1]
    return raw_url


def extract_urls_from_text(text: str) -> list[str]:
    urls: list[str] = []
    for match in re.finditer(r"https?://[^\s<>\]\)\"']+", text):
        url = normalize_url(match.group(0))
        if url.startswith(("http://", "https://")):
            urls.append(url)
    return sorted(dict.fromkeys(urls))


def collect_urls(paths: list[Path], explicit_urls: list[str], urls_file: Path | None) -> list[str]:
    urls: list[str] = []
    for raw_url in explicit_urls:
        urls.append(normalize_url(raw_url))
    if urls_file:
        urls.extend(extract_urls_from_text(urls_file.read_text(encoding="utf-8", errors="replace")))
    for path in paths:
        urls.extend(extract_urls_from_text(path.read_text(encoding="utf-8", errors="replace")))
    return sorted({url for url in urls if url.startswith(("http://", "https://"))})


def load_manifest_entries(path: Path) -> dict[str, dict[str, str]]:
    if not path.exists():
        return {}
    text = path.read_text(encoding="utf-8", errors="replace")
    entries: dict[str, dict[str, str]] = {}
    current: dict[str, str] | None = None
    for line in text.splitlines():
        start = re.match(r"\s*-\s+url_hash:\s+(.+)", line)
        key_value = re.match(r"\s{4}([a-zA-Z0-9_]+):\s+(.+)", line)
        if start:
            current = {"url_hash": json.loads(start.group(1)) if start.group(1).startswith('"') else start.group(1).strip()}
            entries[current["url_hash"]] = current
        elif current is not None and key_value:
            key, raw_value = key_value.groups()
            raw_value = raw_value.strip()
            try:
                value = json.loads(raw_value)
            except json.JSONDecodeError:
                value = raw_value
            current[key] = value
    return entries


def write_manifest(path: Path, entries: dict[str, dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Localized evidence manifest.",
        "# Managed by scripts/localize_evidence.py.",
        "entries:",
    ]
    for key in sorted(entries):
        entry = entries[key]
        lines.append(f"  - url_hash: {quote_yaml(entry['url_hash'])}")
        for field in [
            "url",
            "title",
            "status",
            "content_type",
            "localized_at",
            "last_checked_at",
            "note_path",
            "raw_path",
            "markdown_path",
            "sha256",
        ]:
            lines.append(f"    {field}: {quote_yaml(entry.get(field, ''))}")
    if not entries:
        lines[-1] = "entries: []"
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def path_exists_from_manifest(entry: dict[str, str]) -> bool:
    note_path = entry.get("note_path", "")
    markdown_path = entry.get("markdown_path", "")
    raw_path = entry.get("raw_path", "")
    required_paths = [p for p in [note_path, markdown_path or raw_path] if p]
    return bool(required_paths) and all((REPO_ROOT / path).exists() for path in required_paths)


def fetch_url(url: str, timeout: int) -> tuple[bytes, str, str, str]:
    request = Request(url, headers={"User-Agent": "CommunalEffortEvidenceLocalizer/1.0"})
    with urlopen(request, timeout=timeout) as response:
        body = response.read()
        final_url = response.geturl()
        content_type = response.headers.get("Content-Type", "").split(";")[0].strip().lower()
        status = str(getattr(response, "status", ""))
        return body, final_url, content_type, status


def extract_title_from_html(body: bytes) -> str:
    sample = body[:200_000].decode("utf-8", errors="replace")
    match = re.search(r"<title[^>]*>(.*?)</title>", sample, flags=re.I | re.S)
    if not match:
        return ""
    return html.unescape(" ".join(match.group(1).split()))


def html_to_markdown(body: bytes) -> str:
    parser = MarkdownExtractor()
    parser.feed(body.decode("utf-8", errors="replace"))
    return parser.markdown()


def write_evidence_note(
    *,
    note_path: Path,
    url: str,
    final_url: str,
    title: str,
    content_type: str,
    status: str,
    raw_rel: str,
    markdown_rel: str,
    digest: str,
    captured_at: str,
    extracted_preview: str,
) -> None:
    note_path.parent.mkdir(parents=True, exist_ok=True)
    preview = "\n".join(("> " + line if line else ">") for line in extracted_preview.splitlines()[:40])
    note = f"""---
url: {quote_yaml(url)}
final_url: {quote_yaml(final_url)}
title: {quote_yaml(title)}
status: {quote_yaml(status)}
content_type: {quote_yaml(content_type)}
captured_at: {quote_yaml(captured_at)}
sha256: {quote_yaml(digest)}
raw_path: {quote_yaml(raw_rel)}
markdown_path: {quote_yaml(markdown_rel)}
---

# Evidence Note

## Source

- URL: {url}
- Final URL: {final_url}
- Retrieved: {captured_at}
- HTTP status: {status}
- Content type: {content_type}
- SHA-256: `{digest}`
- Raw capture: `{raw_rel}`
- Local Markdown: `{markdown_rel}`

## Agent Review Notes

- Confirm the organization still exists and is accurately represented.
- Confirm local relevance, active status, contact pathways, and category fit before importing opportunity data.
- Prefer this local evidence note and raw capture before re-fetching the source URL.

## Extract Preview

{preview if preview else '> No text preview was extracted. Review the raw capture instead.'}
"""
    note_path.write_text(note, encoding="utf-8")


def localize_url(url: str, timeout: int) -> dict[str, str]:
    key = url_hash(url)
    host = safe_hostname(url)
    capture_dir = RAW_DIR / host / key
    note_path = NOTES_DIR / host / f"{key}.md"
    capture_dir.mkdir(parents=True, exist_ok=True)
    body, final_url, content_type, status = fetch_url(url, timeout)
    digest = hashlib.sha256(body).hexdigest()
    is_pdf = content_type == "application/pdf" or urlparse(final_url).path.lower().endswith(".pdf")
    is_html = "html" in content_type or content_type in {"", "text/html"}
    extension = ".pdf" if is_pdf else ".html" if is_html else ".txt"
    raw_path = capture_dir / f"source{extension}"
    raw_path.write_bytes(body)
    markdown_path = capture_dir / "source.md"
    title = ""
    if is_pdf:
        markdown = "PDF source captured locally. Review the raw PDF for evidence.\n"
        title = Path(urlparse(final_url).path).name or "PDF source"
    elif is_html:
        markdown = html_to_markdown(body)
        title = extract_title_from_html(body)
    else:
        markdown = body.decode("utf-8", errors="replace")
    markdown_path.write_text(markdown, encoding="utf-8")
    captured_at = today()
    raw_rel = str(raw_path.relative_to(REPO_ROOT))
    markdown_rel = str(markdown_path.relative_to(REPO_ROOT))
    note_rel = str(note_path.relative_to(REPO_ROOT))
    write_evidence_note(
        note_path=note_path,
        url=url,
        final_url=final_url,
        title=title,
        content_type=content_type,
        status=status,
        raw_rel=raw_rel,
        markdown_rel=markdown_rel,
        digest=digest,
        captured_at=captured_at,
        extracted_preview=markdown,
    )
    return {
        "url_hash": key,
        "url": url,
        "title": title,
        "status": status,
        "content_type": content_type,
        "localized_at": captured_at,
        "last_checked_at": captured_at,
        "note_path": note_rel,
        "raw_path": raw_rel,
        "markdown_path": markdown_rel,
        "sha256": digest,
    }


def write_report(results: list[dict[str, str]]) -> tuple[Path, Path]:
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    stem = f"{timestamp()}_evidence-localization"
    json_path = REPORTS_DIR / f"{stem}.json"
    md_path = REPORTS_DIR / f"{stem}.md"
    json_path.write_text(json.dumps(results, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    counts: dict[str, int] = {}
    for result in results:
        counts[result["action"]] = counts.get(result["action"], 0) + 1
    lines = [
        "# Evidence Localization Report",
        "",
        "## Summary",
        "",
    ]
    for action in sorted(counts):
        lines.append(f"- {action}: {counts[action]}")
    lines.extend(["", "## Results", ""])
    for result in results:
        target = result.get("note_path") or result.get("error") or ""
        lines.append(f"- {result['action']}: {result['url']} {target}")
    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return json_path, md_path


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Localize source URLs into ./evidence.")
    parser.add_argument("--from", dest="from_paths", action="append", default=[], help="Read URLs from a report, chapter page, or other text file.")
    parser.add_argument("--url", dest="urls", action="append", default=[], help="Explicit URL to localize. May be passed multiple times.")
    parser.add_argument("--urls-file", type=Path, help="Text file containing URLs to localize.")
    parser.add_argument("--refresh", action="store_true", help="Fetch URLs even when existing manifest entries and local files are present.")
    parser.add_argument("--dry-run", action="store_true", help="Report what would happen without fetching or writing files.")
    parser.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT_SECONDS, help="Fetch timeout in seconds.")
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    from_paths = [Path(path) for path in args.from_paths]
    missing_paths = [str(path) for path in from_paths if not path.exists()]
    if missing_paths:
        print("Missing --from path(s): " + ", ".join(missing_paths), file=sys.stderr)
        return 2
    if args.urls_file and not args.urls_file.exists():
        print(f"Missing --urls-file path: {args.urls_file}", file=sys.stderr)
        return 2
    urls = collect_urls(from_paths, args.urls, args.urls_file)
    manifest = load_manifest_entries(MANIFEST_PATH)
    results: list[dict[str, str]] = []
    if args.dry_run:
        for url in urls:
            existing = manifest.get(url_hash(url))
            action = "would-refresh" if args.refresh and existing else "would-skip" if existing and path_exists_from_manifest(existing) else "would-localize"
            results.append({"action": action, "url": url, "note_path": existing.get("note_path", "") if existing else ""})
        print_summary(results, dry_run=True)
        return 0
    EVIDENCE_ROOT.mkdir(exist_ok=True)
    NOTES_DIR.mkdir(parents=True, exist_ok=True)
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    for url in urls:
        key = url_hash(url)
        existing = manifest.get(key)
        if existing and not args.refresh and path_exists_from_manifest(existing):
            results.append({"action": "skipped", "url": url, "note_path": existing.get("note_path", ""), "raw_path": existing.get("raw_path", "")})
            continue
        try:
            entry = localize_url(url, args.timeout)
            manifest[key] = entry
            results.append({"action": "localized", "url": url, "note_path": entry["note_path"], "raw_path": entry["raw_path"], "markdown_path": entry["markdown_path"]})
        except (HTTPError, URLError, TimeoutError, OSError) as error:
            results.append({"action": "failed", "url": url, "error": f"{type(error).__name__}: {error}"})
    write_manifest(MANIFEST_PATH, manifest)
    json_report, markdown_report = write_report(results)
    results.append({"action": "report", "url": "", "note_path": str(markdown_report.relative_to(REPO_ROOT)), "raw_path": str(json_report.relative_to(REPO_ROOT))})
    print_summary(results, dry_run=False)
    return 1 if any(result["action"] == "failed" for result in results) else 0


def print_summary(results: list[dict[str, str]], *, dry_run: bool) -> None:
    counts: dict[str, int] = {}
    for result in results:
        counts[result["action"]] = counts.get(result["action"], 0) + 1
    label = "Evidence localization dry run" if dry_run else "Evidence localization"
    print(label)
    for action in sorted(counts):
        print(f"- {action}: {counts[action]}")
    for result in results:
        if result["action"] in {"localized", "skipped", "failed", "would-localize", "would-skip", "would-refresh"}:
            detail = result.get("note_path") or result.get("error") or ""
            print(f"{result['action']}: {result['url']} {detail}")
        elif result["action"] == "report":
            print(f"report: {result.get('note_path')} ({result.get('raw_path')})")


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
