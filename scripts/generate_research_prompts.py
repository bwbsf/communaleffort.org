#!/usr/bin/env python3
"""Generate ignored deep-research prompt artifacts for missing chapter-category targets."""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path
from string import Template
from typing import Iterable

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_TEMPLATE = REPO_ROOT / "templates" / "deep_research_opportunity_prompt.md"
DEFAULT_OUTPUT_DIR = REPO_ROOT / "research" / "generated"
FRONT_MATTER_BOUNDARY = "---"
TOP_LEVEL_KEY_PATTERN = re.compile(r"^([A-Za-z0-9_]+):(?:\s*(.*))?$")
CATEGORY_SLUG_PATTERN = re.compile(r"^\s*-?\s*category_slug:\s*['\"]?([^'\"\s]+)['\"]?")
PLACEHOLDER_PATTERN = re.compile(r"{{\s*([A-Za-z0-9_]+)\s*}}")


@dataclass(frozen=True)
class Category:
    title: str
    slug: str
    description: str
    examples: tuple[str, ...]


@dataclass(frozen=True)
class Chapter:
    title: str
    slug: str
    path: Path
    rel_path: str
    continent_name: str
    metro_or_region: str
    city_or_area: str
    state_or_province: str
    country: str
    official_url: str
    focus_areas: tuple[str, ...]
    source_urls: tuple[str, ...]
    existing_category_slugs: frozenset[str]


def extract_front_matter(path: Path) -> list[str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    if len(lines) < 3 or lines[0].strip() != FRONT_MATTER_BOUNDARY:
        raise ValueError(f"{path} is missing YAML front matter")

    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == FRONT_MATTER_BOUNDARY:
            return lines[1:index]

    raise ValueError(f"{path} is missing a closing YAML front matter boundary")


def unquote(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        return value[1:-1]
    return value


def parse_simple_front_matter(path: Path) -> dict[str, object]:
    lines = extract_front_matter(path)
    data: dict[str, object] = {}
    index = 0

    while index < len(lines):
        line = lines[index]
        match = TOP_LEVEL_KEY_PATTERN.match(line)
        if not match:
            index += 1
            continue

        key, raw_value = match.groups()
        raw_value = (raw_value or "").strip()
        if raw_value == "[]":
            data[key] = []
            index += 1
            continue
        if raw_value:
            data[key] = unquote(raw_value)
            index += 1
            continue

        values: list[str] = []
        nested_index = index + 1
        while nested_index < len(lines) and not TOP_LEVEL_KEY_PATTERN.match(lines[nested_index]):
            nested_line = lines[nested_index].strip()
            if nested_line.startswith("- "):
                item = nested_line[2:].strip()
                if item:
                    values.append(unquote(item))
            nested_index += 1
        data[key] = values
        index = nested_index

    return data


def parse_existing_opportunity_category_slugs(path: Path) -> frozenset[str]:
    lines = extract_front_matter(path)
    slugs: set[str] = set()
    in_opportunities = False

    for line in lines:
        if line.startswith("opportunities:"):
            in_opportunities = True
            continue
        if in_opportunities and TOP_LEVEL_KEY_PATTERN.match(line):
            break
        if in_opportunities:
            match = CATEGORY_SLUG_PATTERN.match(line)
            if match:
                slugs.add(match.group(1))

    return frozenset(slugs)


def as_tuple(value: object) -> tuple[str, ...]:
    if isinstance(value, list):
        return tuple(str(item) for item in value if str(item).strip())
    if isinstance(value, str) and value.strip():
        return (value,)
    return ()


def discover_categories(categories_dir: Path) -> list[Category]:
    categories: list[Category] = []
    for path in sorted(categories_dir.glob("*/index.md")):
        data = parse_simple_front_matter(path)
        slug = str(data.get("category_slug") or path.parent.name)
        categories.append(
            Category(
                title=str(data.get("title") or slug),
                slug=slug,
                description=str(data.get("description") or ""),
                examples=as_tuple(data.get("examples")),
            )
        )
    return sorted(categories, key=lambda category: category.slug)


def discover_chapters(chapters_dir: Path) -> list[Chapter]:
    chapters: list[Chapter] = []
    for path in sorted(chapters_dir.glob("*/*/index.md")):
        data = parse_simple_front_matter(path)
        rel_path = path.relative_to(REPO_ROOT).as_posix()
        chapters.append(
            Chapter(
                title=str(data.get("title") or path.parent.name),
                slug=str(data.get("chapter_slug") or path.parent.name),
                path=path,
                rel_path=rel_path,
                continent_name=str(data.get("continent_name") or ""),
                metro_or_region=str(data.get("metro_or_region") or path.parent.name),
                city_or_area=str(data.get("city_or_area") or data.get("metro_or_region") or path.parent.name),
                state_or_province=str(data.get("state_or_province") or ""),
                country=str(data.get("country") or ""),
                official_url=str(data.get("official_url") or ""),
                focus_areas=as_tuple(data.get("focus_areas")),
                source_urls=as_tuple(data.get("sources")),
                existing_category_slugs=parse_existing_opportunity_category_slugs(path),
            )
        )
    return sorted(chapters, key=lambda chapter: (chapter.continent_name, chapter.city_or_area, chapter.title))


def render_list(values: Iterable[str], empty: str = "None listed") -> str:
    items = [value for value in values if value]
    if not items:
        return empty
    return ", ".join(items)


def render_target_list(categories: list[Category]) -> str:
    lines: list[str] = []
    for category in categories:
        lines.append(f"- `{category.slug}` — {category.title}: {category.description}")
        if category.examples:
            lines.append(f"  - Examples: {', '.join(category.examples)}")
    return "\n".join(lines)


def render_prompt(template_text: str, chapter: Chapter, missing_categories: list[Category]) -> str:
    context = {
        "chapter_title": chapter.title,
        "chapter_slug": chapter.slug,
        "chapter_path": chapter.rel_path,
        "continent_name": chapter.continent_name or "Unknown",
        "metro_or_region": chapter.metro_or_region or "Unknown",
        "city_or_area": chapter.city_or_area or "Unknown",
        "state_or_province": chapter.state_or_province or "Unknown",
        "country": chapter.country or "Unknown",
        "official_url": chapter.official_url or "None listed",
        "focus_areas": render_list(chapter.focus_areas),
        "source_urls": render_list(chapter.source_urls),
        "target_list": render_target_list(missing_categories),
    }
    template_text = PLACEHOLDER_PATTERN.sub(r"${\1}", template_text)
    return Template(template_text).safe_substitute(context).rstrip() + "\n"


def write_json(path: Path, payload: object) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def generate(args: argparse.Namespace) -> None:
    categories = discover_categories(args.categories_dir)
    chapters = discover_chapters(args.chapters_dir)
    template_text = args.template.read_text(encoding="utf-8")
    prompts_dir = args.output_dir / "prompts"
    prompts_dir.mkdir(parents=True, exist_ok=True)

    manifest: list[dict[str, object]] = []
    total_missing_targets = 0

    for chapter in chapters:
        missing_categories = [category for category in categories if category.slug not in chapter.existing_category_slugs]
        total_missing_targets += len(missing_categories)
        prompt_path = prompts_dir / chapter.continent_name.lower().replace(" ", "-") / f"{chapter.metro_or_region}.md"
        prompt_path.parent.mkdir(parents=True, exist_ok=True)
        prompt_path.write_text(render_prompt(template_text, chapter, missing_categories), encoding="utf-8")
        manifest.append(
            {
                "chapter_title": chapter.title,
                "chapter_slug": chapter.slug,
                "chapter_path": chapter.rel_path,
                "city_or_area": chapter.city_or_area,
                "continent_name": chapter.continent_name,
                "missing_target_count": len(missing_categories),
                "missing_category_slugs": [category.slug for category in missing_categories],
                "prompt_path": prompt_path.relative_to(REPO_ROOT).as_posix(),
            }
        )

    args.output_dir.mkdir(parents=True, exist_ok=True)
    write_json(
        args.output_dir / "missing-research-targets.json",
        {
            "chapter_count": len(chapters),
            "category_count": len(categories),
            "missing_target_count": total_missing_targets,
            "chapters": manifest,
        },
    )

    print(f"Chapters: {len(chapters)}")
    print(f"Categories: {len(categories)}")
    print(f"Missing chapter-category targets: {total_missing_targets}")
    print(f"Prompt artifacts: {len(chapters)}")
    print(f"Output directory: {args.output_dir.relative_to(REPO_ROOT).as_posix()}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--chapters-dir", type=Path, default=REPO_ROOT / "chapters")
    parser.add_argument("--categories-dir", type=Path, default=REPO_ROOT / "categories")
    parser.add_argument("--template", type=Path, default=DEFAULT_TEMPLATE)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    return parser.parse_args()


def main() -> None:
    generate(parse_args())


if __name__ == "__main__":
    main()
