import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import os

# -------------------------------------------------
# 1. Load data
# -------------------------------------------------

# Project root = parent of the src folder where this file lives
PROJECT_ROOT = Path(__file__).resolve().parents[1]

# Path to the processed data file
data_path = PROJECT_ROOT / "data" / "processed" / "student_scores_clean.csv"

df = pd.read_csv(data_path)

# Columns for the 7 subjects in this dataset
score_cols = [
    "math_score",
    "history_score",
    "physics_score",
    "chemistry_score",
    "biology_score",
    "english_score",
    "geography_score",
]

# -------------------------------------------------
# 2. Create average score across subjects
# -------------------------------------------------
df["average_score"] = df[score_cols].mean(axis=1)

# -------------------------------------------------
# 3. Boxplot: average score by study-hours quartile
# -------------------------------------------------
# Create quartile bins for weekly self-study hours
df["study_bin"] = pd.qcut(
    df["weekly_self_study_hours"],
    q=4,
    labels=["Low", "Med-Low", "Med-High", "High"]
)

plt.figure(figsize=(6, 4))
df.boxplot(column="average_score", by="study_bin")
plt.suptitle("")  # Remove the automatic suptitle from pandas
plt.title("Average Score by Study Hours Quartile")
plt.xlabel("Study Hours Quartile")
plt.ylabel("Average Score")
plt.tight_layout()
# If you want to save instead of show:
plt.savefig(os.path.join(PROJECT_ROOT,"results","figures","boxplot_study.pdf"))

# -------------------------------------------------
# 4. Boxplot: average score by absence-days quartile
# -------------------------------------------------
df["absence_bin"] = pd.qcut(
    df["absence_days"],
    q=4,
    labels=["Low", "Med-Low", "Med-High", "High"]
)

plt.figure(figsize=(6, 4))
df.boxplot(column="average_score", by="absence_bin")
plt.suptitle("")
plt.title("Average Score by Absence Days Quartile")
plt.xlabel("Absence Days Quartile")
plt.ylabel("Average Score")
plt.tight_layout()
plt.show()
plt.savefig(os.path.join(PROJECT_ROOT,"results","figures","boxplot_absence.pdf"))
