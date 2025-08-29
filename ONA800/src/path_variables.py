from datetime import datetime
from pathlib import Path

# Directories
ROOT_DIR = Path(__file__).parent.parent
RESULTS_DIR = ROOT_DIR / "output"
_now = datetime.now()
_file_name = _now.strftime("%Y-%m-%d-%H-%M.txt")
RESULT_FILE = RESULTS_DIR / _file_name
