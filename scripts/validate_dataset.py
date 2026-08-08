#!/usr/bin/env python3

import argparse
import json
from pathlib import Path

from jsonschema import Draft202012Validator


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def validate_jsonl(dataset_path: Path, schema_path: Path) -> int:
    schema = load_json(schema_path)
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema)

    seen_ids = set()
    errors = 0
    records = 0

    with dataset_path.open("r", encoding="utf-8") as f:
        for line_number, raw_line in enumerate(f, start=1):
            line = raw_line.strip()
            if not line:
                continue

            records += 1
            try:
                record = json.loads(line)
            except json.JSONDecodeError as exc:
                print(f"line {line_number}: invalid JSON: {exc}")
                errors += 1
                continue

            record_id = record.get("id")
            if record_id in seen_ids:
                print(f"line {line_number}: duplicate id: {record_id}")
                errors += 1
            elif record_id:
                seen_ids.add(record_id)

            validation_errors = sorted(
                validator.iter_errors(record), key=lambda e: list(e.path)
            )
            for error in validation_errors:
                location = ".".join(str(part) for part in error.path) or "record"
                print(f"line {line_number} [{location}]: {error.message}")
                errors += 1

            messages = record.get("messages", [])
            if messages and messages[-1].get("role") != "assistant":
                print(f"line {line_number} [messages]: final message must be assistant")
                errors += 1

    if errors:
        print(f"FAIL: {errors} error(s) across {records} record(s)")
        return 1

    print(f"OK: {records} record(s) validated")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate OrbeAI SFT JSONL datasets")
    parser.add_argument("dataset", type=Path, help="Path to JSONL dataset")
    parser.add_argument(
        "--schema",
        type=Path,
        default=Path("datasets/schemas/sft-v0.1.schema.json"),
        help="Path to JSON Schema",
    )
    args = parser.parse_args()
    return validate_jsonl(args.dataset, args.schema)


if __name__ == "__main__":
    raise SystemExit(main())
