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


def write_csv_file(csv_path, collumns, lines):
    with open(csv_path, 'w') as f:
        csv_writer = csv.DictWriter(
            f,
            fieldnames=collumns,
            lineterminator='\n'
        )
        csv_writer.writeheader()

        for line in lines:
            csv_writer.writerow(line)


def get_headers():
    ...


if __name__ == "__main__":
    base_dir = Path(__file__).parent
    resource_dir = base_dir / "resource"
    result_dir = base_dir / "result"
    output_json = result_dir / "merged.json"
    output_csv = result_dir / "output.csv"

    merge_json_files(resource_dir, output_json)

    with open(output_json, 'r') as f:
        json_list = json.load(f)
        collumns = json_list[0]
        # print(collumns)
        # for key, value in collumns.items():
        #     if isinstance(value, list):
        #         print(key, 'lista')
        write_csv_file(output_csv, collumns, json_list)
