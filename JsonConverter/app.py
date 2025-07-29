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


def json_map(source, parent_key=''):
    flat_dict = {}

    if isinstance(source, dict):
        for key, value in source.items():
            full_key = f"{parent_key}_{key}" if parent_key else key
            if isinstance(value, dict):
                flat_dict.update(json_map(value, full_key))
            elif isinstance(value, list):
                if value and isinstance(value[0], (dict, list)):
                    flat_dict.update(json_map(value[0], full_key))
                else:
                    flat_dict[full_key] = value
            else:
                flat_dict[full_key] = value

    elif isinstance(source, list):
        for i, item in enumerate(source):
            flat_dict.update(json_map(item, parent_key))

    return flat_dict


def write_csv(csv_path, resource, json_list):
    collumns = []
    for key in resource.keys():
        collumns.append(key)

    with open(csv_path, 'w') as f:
        csv_writer = csv.DictWriter(
            f,
            fieldnames=collumns
        )
        csv_writer.writeheader()

        for item in json_list:
            if isinstance(item, dict):
                for value in resource.values():
                    csv_writer.writerow(value)


if __name__ == "__main__":
    base_dir = Path(__file__).parent
    resource_dir = base_dir / "resource"
    result_dir = base_dir / "result"
    output_json = result_dir / "merged.json"
    output_csv = result_dir / "output.csv"

    merge_json_files(resource_dir, output_json)

    with open(output_json, 'r') as f:
        json_list = json.load(f)
        resource_dict = json_map(json_list)

        write_csv(output_csv, resource_dict, json_list)
