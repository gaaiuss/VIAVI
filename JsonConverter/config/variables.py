from pathlib import Path

# Directories
ROOT_DIR = Path(__file__).parent.parent
RESOURCE_DIR = ROOT_DIR / "resource"
RESULT_DIR = ROOT_DIR / "output"
CONFIG_DIR = Path(__file__).parent
IMG_DIR = ROOT_DIR / "img"

# Files
JSON_OUTPUT_FILE = CONFIG_DIR / "merged.json"
CSV_CONFIG_FILE = CONFIG_DIR / "config.csv"
CSV_OUTPUT_FILE = RESULT_DIR / "output.csv"

# GUI
ICON_PATH = IMG_DIR / "icon.png"

# Sizing
BIG_FONT_SIZE = 40
MEDIUM_FONT_SIZE = 24
SMALL_FONT_SIZE = 12
MINIMUM_WIDTH = 1000
TEXT_MARGIN = 10
