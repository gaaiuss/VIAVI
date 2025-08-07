import os
from pathlib import Path

# Directories
ROOT_DIR = Path(__file__).parent.parent
RESOURCE_DIR = ROOT_DIR / "resource"
RESULT_DIR = ROOT_DIR / "output"
CONFIG_DIR = Path(__file__).parent

os.mkdir(RESOURCE_DIR)

# Files
JSON_OUTPUT_FILE = CONFIG_DIR / "merged.json"
CSV_CONFIG_FILE = CONFIG_DIR / "config.csv"
CSV_OUTPUT_FILE = RESULT_DIR / "output.csv"
