import csv
import json
from pathlib import Path


def merge_json_files(json_files: list[str], output_file: 'Path') -> None:
    merged_data = []

    for file_path in json_files:
        path_obj = Path(file_path)
        with open(path_obj, 'r', encoding='utf8') as f:
            data = json.load(f)
            if isinstance(data, list):
                merged_data.extend(data)
            else:
                merged_data.append(data)

    with open(output_file, 'w', encoding='utf8') as f:
        json.dump(merged_data, f)


def flatten_json_list(json_list: list[dict]) -> list[dict]:
    def flatten(obj, parent_key='', result=None):
        if result is None:
            result = {}
        if isinstance(obj, dict):
            for k, v in obj.items():
                full_key = f"{parent_key}.{k}" if parent_key else k
                flatten(v, full_key, result)
        elif isinstance(obj, list) and all(
            isinstance(i, (dict, list)) for i in obj
        ):
            for idx, item in enumerate(obj):
                flatten(item, parent_key, result)
        else:
            result[parent_key] = obj
        return result

    flattened_list = []
    for item in json_list:
        flat = flatten(item)
        flattened_list.append(flat)
    return flattened_list


def format_4ascii_4hex(serial: list[int]) -> str:
    ascii_part = ''.join(chr(b) for b in serial[:4])
    hex_part = ''.join(f'{b:02X}' for b in serial[4:])
    return f"{ascii_part}-{hex_part}"


def format_serial_number(json_list: list[dict]) -> list[dict]:
    fmt_json = []
    for json_obj in json_list:
        for test in json_obj.get("tests", []):
            serial_path = test.get("results", {}).get(
                "data", {}).get("gpon", {})
            if isinstance(serial_path.get("ontSerialNumber"), list):
                serial_number = serial_path["ontSerialNumber"]
                formatted_serial = format_4ascii_4hex(serial_number)
                serial_path["ontSerialNumber"] = formatted_serial
        fmt_json.append(json_obj)
    return fmt_json


def load_column_order(csv_config: Path) -> list[str]:
    with open(csv_config, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return [row['column'] for row in sorted(
            reader,
            key=lambda r: int(r['order'])
        )]


def write_csv(csv_path: Path, csv_config: Path, resource: list[dict]) -> None:
    column_order = load_column_order(csv_config)

    with open(csv_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=column_order)
        writer.writeheader()

        for row in resource:
            ordered_row = {col: row.get(col, '') for col in column_order}
            writer.writerow(ordered_row)
