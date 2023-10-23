from pathlib import Path

CATEGORICAL_COLS = COLUMNS TO DERTERMINE #["PULocationID", "DOLocationID", "passenger_count"]

# [3] means go up 3 levels from the current file -> from ./src/modelling/config.py to ./
PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIRPATH = str(PROJECT_ROOT / "data")
MODELS_DIRPATH = str(PROJECT_ROOT / "src"/"modelling")
