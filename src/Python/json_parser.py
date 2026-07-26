# json_parser.py
import json
from typing import Any, Callable, List, Dict, Tuple


def read_json_file(path: str) -> Any:
    """Read and parse JSON file safely."""
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def write_json_file(path: str, data: Any) -> None:
    """Write JSON data to a file."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def get_all_keys(data: Any) -> List[str]:
    """Return all unique keys in a nested JSON structure."""
    keys = set()

    def walk(node):
        if isinstance(node, dict):
            for k, v in node.items():
                keys.add(k)
                walk(v)
        elif isinstance(node, list):
            for item in node:
                walk(item)

    walk(data)
    return sorted(keys)


def traverse_json(data: Any, field: str):
    """Yield all values for a given field anywhere in the JSON."""
    if isinstance(data, dict):
        for k, v in data.items():
            if k == field:
                yield v
            yield from traverse_json(v, field)

    elif isinstance(data, list):
        for item in data:
            yield from traverse_json(item, field)


def parse_items(
    items: List[Dict],
    fields: List[str],
    match_fn: Callable[[Any], bool],
    progress_cb: Callable[[int], None] | None = None
) -> Tuple[List[Dict], List[Dict]]:
    """
    Generic parser: returns (result_items, found_items)
    found_items = items where match_fn(value) is True
    result_items = everything else
    """

    result_items = []
    found_items = []

    total = len(items) * len(fields)
    processed = 0

    for field in fields:
        for item in items:
            matched = False

            for value in traverse_json(item, field):
                if match_fn(value):
                    matched = True
                    if item not in found_items:
                        found_items.append(item)
                else:
                    matched = True
                    if item not in result_items:
                        result_items.append(item)

            if not matched and item not in found_items and item not in result_items:
                result_items.append(item)

            processed += 1
            if progress_cb:
                progress_cb(int(processed / total * 100))

    return result_items, found_items


def parse_duplicates(items: List[Dict], fields: List[str], progress_cb=None):
    seen = set()

    def is_dup(value):
        if value and value not in seen:
            seen.add(value)
            return True
        return False

    return parse_items(items, fields, is_dup, progress_cb)


def parse_empty(items: List[Dict], fields: List[str], progress_cb=None):
    return parse_items(items, fields, lambda v: v == "", progress_cb)


def parse_null(items: List[Dict], fields: List[str], progress_cb=None):
    return parse_items(items, fields, lambda v: v is None, progress_cb)
