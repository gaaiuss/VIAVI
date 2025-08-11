import csv
import json
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pathlib import Path


def merge_json_files(resource_dir: 'Path', output_file: 'Path') -> None:
    """
    Merge multiple JSON files from a directory into a single JSON file.

    Reads all JSON files in the given directory. If a file contains a list,
    extends the merged list with its elements; if it contains a dict, appends
    it as an item.

    Args:
        resource_dir (Path): Directory containing JSON files to merge.
        output_file (Path): Path to save the merged JSON output.
    """
    json_files = resource_dir.glob("*.json")
    merged_data = []

    for file_path in json_files:
        with open(file_path, 'r', encoding='utf8') as f:
            data = json.load(f)
            if isinstance(data, list):
                merged_data.extend(data)
            else:
                merged_data.append(data)

    with open(output_file, 'w', encoding='utf8') as f:
        json.dump(merged_data, f, indent=2)


def flatten_json_list(json_list: list[dict]) -> list[dict]:
    """
    Flatten a list of nested JSON dictionaries into a list of flat
    dictionaries.

    Nested keys are concatenated with '.' to create a single-level dictionary.

    Lists of dicts or nested lists are recursively flattened.

    Args:
        json_list (list[dict]): List of nested dictionaries to flatten.

    Returns:
        list[dict]: List of flattened dictionaries with dot-notated keys.
    """
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
    """
    Format a serial number represented as a list of integers into a string with
    ASCII and hexadecimal parts.

    The first 4 bytes are converted to ASCII characters.
    The remaining bytes are converted to uppercase hex digits.

    Args:
        serial (list[int]): List of integers representing the serial number
        bytes.

    Returns:
        str: Formatted string in 'ASCII-HEX' pattern, e.g. 'MSTC-FF00A3'.
    """
    ascii_part = ''.join(chr(b) for b in serial[:4])
    hex_part = ''.join(f'{b:02X}' for b in serial[4:])
    return f"{ascii_part}-{hex_part}"


def format_serial_number(json_list: list[dict]) -> list[dict]:
    """
    Format the 'ontSerialNumber' field inside each test in a JSON list.

    If 'ontSerialNumber' is a list of integers, formats it using
    `format_4ascii_4hex` and updates the JSON object in-place.

    Args:
        json_list (list[dict]): List of JSON objects containing 'tests' key.

    Returns:
        list[dict]: The updated list with formatted serial numbers.
    """
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


def load_column_order(csv_config: 'Path') -> list[str]:
    """
    Load the desired CSV column order from a configuration CSV file.

    The config file should have 'column' and 'order' headers; columns
    are sorted by 'order' ascending.

    Args:
        csv_config (Path): Path to the CSV configuration file.

    Returns:
        list[str]: List of column names ordered as specified in the config.
    """
    with open(csv_config, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return [row['column'] for row in sorted(
            reader,
            key=lambda r: int(r['order'])
        )]


def write_csv(
        csv_path: 'Path', csv_config: 'Path', resource: list[dict]
) -> None:
    """
    Write a list of dictionaries to a CSV file using a specified column order.

    Loads the column order from a config CSV file, then writes the resource
    data rows ordered by those columns. Missing columns in a row are filled
    with empty strings.

    Args:
        csv_path (Path): Output path for the CSV file.
        csv_config (Path): Path to the CSV config specifying column order.
        resource (list[dict]): List of dictionaries representing CSV rows.
    """
    column_order = load_column_order(csv_config)

    with open(csv_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=column_order)
        writer.writeheader()

        for row in resource:
            ordered_row = {col: row.get(col, '') for col in column_order}
            writer.writerow(ordered_row)
