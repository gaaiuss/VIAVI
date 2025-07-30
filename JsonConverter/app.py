import json
import csv
from pathlib import Path


def merge_json_files(resource_dir: Path, output_file: Path):
    json_files = resource_dir.glob("*.json")
    merged_data = []

    for file_path in json_files:
        try:
            with open(file_path, 'r', encoding='utf8') as f:
                data = json.load(f)
                if isinstance(data, list):
                    merged_data.extend(data)
                else:
                    merged_data.append(data)
        except (json.JSONDecodeError, OSError) as e:
            print(f"Warning: Failed to process {file_path.name}: {e}")

    with open(output_file, 'w', encoding='utf8') as f:
        json.dump(merged_data, f, indent=2)


def flatten_json_list(json_list: list):
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


def format_serial_number(json_list: list):
    fmt_json = []
    for json_obj in json_list:
        for test in json_obj.get("tests", []):
            serial_path = test.get("results", {}).get(
                "data", {}).get("gpon", {})
            if isinstance(serial_path.get("ontSerialNumber"), list):
                serial_number = serial_path["ontSerialNumber"]
                str_serial = '-'.join(str(num) for num in serial_number)
                serial_path["ontSerialNumber"] = str_serial
        fmt_json.append(json_obj)
    return fmt_json


def write_csv(csv_path: Path, resource: dict):
    with open(csv_path, 'w', newline='', encoding='utf-8') as f:
        for dict_ in resource:
            collumns = dict_.keys()
        writer = csv.DictWriter(f, fieldnames=collumns)
        writer.writeheader()
        for dict_ in resource:
            writer.writerow(dict_)


if __name__ == "__main__":
    base_dir = Path(__file__).parent
    resource_dir = base_dir / "resource"
    result_dir = base_dir / "result"
    output_json = result_dir / "merged.json"
    output_csv = result_dir / "output.csv"

    merge_json_files(resource_dir, output_json)

    with open(output_json, 'r') as f:
        json_list = json.load(f)
        fmt_json = format_serial_number(json_list)
        resource = flatten_json_list(fmt_json)
        write_csv(output_csv, resource)
