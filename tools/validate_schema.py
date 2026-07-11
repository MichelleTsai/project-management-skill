#!/usr/bin/env python3
"""
validate_schema.py

簡單的 schema 驗證工具：比對 sample JSON/CSV 的欄位與預期 schema（JSON 格式），
產生差異報告。設計成通用工具，不包含任何專案或人名資訊。
用法：python tools/validate_schema.py --schema schema.json --sample sample.json
"""
import argparse
import json
import csv
import sys
from typing import Set


def load_schema(schema_path: str) -> Set[str]:
    with open(schema_path, 'r', encoding='utf-8') as f:
        schema = json.load(f)
    # schema expected as list of field names or dict with 'fields'
    if isinstance(schema, list):
        return set(schema)
    if isinstance(schema, dict) and 'fields' in schema:
        return set(schema['fields'])
    # fallback: assume keys of dict
    if isinstance(schema, dict):
        return set(schema.keys())
    raise ValueError('Unsupported schema format')


def load_sample_json(path: str) -> Set[str]:
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    # if it's a list, take first object
    if isinstance(data, list) and data:
        data = data[0]
    if isinstance(data, dict):
        return set(data.keys())
    raise ValueError('Unsupported sample JSON format')


def load_sample_csv(path: str) -> Set[str]:
    with open(path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        headers = next(reader, None)
        if headers:
            return set([h.strip() for h in headers])
    raise ValueError('CSV has no header')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--schema', required=True, help='Path to expected schema (JSON)')
    parser.add_argument('--sample', required=True, help='Path to sample (JSON or CSV)')
    args = parser.parse_args()

    schema_fields = load_schema(args.schema)
    sample = args.sample
    if sample.lower().endswith('.csv'):
        sample_fields = load_sample_csv(sample)
    else:
        sample_fields = load_sample_json(sample)

    missing = schema_fields - sample_fields
    extra = sample_fields - schema_fields

    report = {
        'schema_fields_count': len(schema_fields),
        'sample_fields_count': len(sample_fields),
        'missing_fields': sorted(list(missing)),
        'extra_fields': sorted(list(extra)),
    }

    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
