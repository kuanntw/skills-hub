#!/usr/bin/env python3
"""Explain lexical routing candidates. Never install, fetch, or execute skills."""
import argparse
from fnmatch import fnmatchcase
import json
import re

from build_index import load_entries


def trigger_matches(query, trigger):
    # English tokens need boundaries: UI must not match build, VC not service.
    # Chinese phrases intentionally support substrings within unspaced prose.
    pattern = re.escape(trigger)
    if re.match(r"[A-Za-z0-9]", trigger):
        pattern = r"(?<![A-Za-z0-9_])" + pattern
    if re.search(r"[A-Za-z0-9]$", trigger):
        pattern += r"(?![A-Za-z0-9_])"
    return re.search(pattern, query, flags=re.IGNORECASE) is not None


def path_matches(path, pattern):
    # Match slash-separated paths. ** spans zero or more segments; * does not.
    def match(parts, rules):
        if not rules:
            return not parts
        if rules[0] == "**":
            return match(parts, rules[1:]) or bool(parts and match(parts[1:], rules))
        return bool(parts and fnmatchcase(parts[0], rules[0]) and match(parts[1:], rules[1:]))

    return match(path.split("/"), pattern.split("/"))


def candidates(entries, query, paths=(), task_types=()):
    results = []
    for entry in entries:
        triggers = [t for t in entry["triggers"] if trigger_matches(query, t)]
        files = [p for p in paths if any(path_matches(p, rule) for rule in entry["related_file_patterns"])]
        tasks = sorted(set(task_types) & set(entry["task_types"]))
        if not (triggers or files or tasks):
            continue
        results.append({
            "id": entry["id"], "type": entry["type"],
            "registry": f"registry/{entry['id']}.json",
            "evidence": {"triggers": triggers, "files": files, "task_types": tasks},
            "use_when": entry["use_when"], "avoid_when": entry["avoid_when"],
            "status": "candidate_requires_context_review",
        })
    return results


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query")
    parser.add_argument("--file", action="append", default=[])
    parser.add_argument("--task-type", action="append", default=[])
    args = parser.parse_args()
    print(json.dumps(candidates(load_entries(), args.query, args.file, args.task_type), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
