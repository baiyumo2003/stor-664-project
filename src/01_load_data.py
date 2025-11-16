"""
01_load_data.py
----------------
Load and clean the student-scores dataset.

Directory Structure (expected):
project/
│
├── data/
│     ├── raw/student-scores.csv
│     └── processed/
│
└── src/01_load_data.py
"""

import pandas as pd
from pathlib import Path


# -----------------------------
# Paths (matches your structure)
# -----------------------------
ROOT = Path(__file__).resolve().parents[1]      # project root directory

DATA_DIR = ROOT / "data" / "raw"
RESULTS_DIR = ROOT / "data" / "processed"

RAW_FILE = DATA_DIR / "student-scores.csv"
OUTPUT_FILE = RESULTS_DIR / "student_scores_clean.csv"

# Ensure processed/ folder exists
RESULTS_DIR.mkdir(exist_ok=True, parents=True)


# -----------------------------
# Helper Functions
# -----------------------------
def clean_column_names(df):
    """Convert all column names to snake_case."""
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("-", "_")
    )
    return df


def ensure_numeric_scores(df):
    """Convert score columns to numeric and remove invalid entries."""
    score_cols = [
        "math_score", "history_score", "physics_score", "chemistry_score",
        "biology_score", "english_score", "geography_score"
    ]

    for col in score_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Drop rows with missing scores
    df = df.dropna(subset=score_cols)

    # Remove impossible scores
    for col in score_cols:
        df = df[(df[col] >= 0) & (df[col] <= 100)]

    return df


def load_data(path=RAW_FILE):
    """Load raw CSV dataset."""
    print(f"Loading dataset from: {path}")
    return pd.read_csv(path)


def clean_data(df):
    """Apply cleaning steps."""
    df = clean_column_names(df)
    df = ensure_numeric_scores(df)
    return df


def main():
    df = load_data()
    df_clean = clean_data(df)

    df_clean.to_csv(OUTPUT_FILE, index=False)
    print(f"Cleaned dataset saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
