import json
import glob
from pathlib import Path

RESOURCE_PATH = 'JsonConverter\\resource\\*.json'
MERGE_PATH = Path(__file__).parent / 'merged.json'

# Step 1: Get all JSON file paths in a folder
json_files = glob.glob(RESOURCE_PATH)

# Step 2: Initialize an empty list to hold all data
merged_data = []

# Step 3: Iterate through files and append their contents to the list
for file in json_files:
    with open(file, 'r', encoding='utf8') as f:
        data = json.load(f)
        if isinstance(data, list):
            merged_data.extend(data)  # if the JSON file contains a list
        else:
            merged_data.append(data)  # if the JSON file contains a single dict

# Step 4: Optionally save the merged list to a new JSON file
with open(MERGE_PATH, 'w', encoding='utf8') as f:
    json.dump(merged_data, f, indent=4, ensure_ascii=False)
