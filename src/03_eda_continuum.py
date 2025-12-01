import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

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
# 3. EDA treating predictors as continuous
#    (scatter + fitted linear trend)
# -------------------------------------------------

def scatter_with_trend(x, y, x_label, y_label, title, filename=None):
    """Make a scatterplot with a simple linear regression line."""
    plt.figure(figsize=(6, 4))

    # Scatter
    plt.scatter(x, y, alpha=0.3)

    # Fit a simple linear regression line using numpy.polyfit
    # degree = 1 for a straight line
    mask = (~pd.isna(x)) & (~pd.isna(y))
    x_clean = x[mask]
    y_clean = y[mask]

    if len(x_clean) > 1:
        beta1, beta0 = np.polyfit(x_clean, y_clean, deg=1)
        x_grid = np.linspace(x_clean.min(), x_clean.max(), 100)
        y_pred = beta1 * x_grid + beta0
        plt.plot(x_grid, y_pred)

    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.tight_layout()

    if filename is not None:
        plt.savefig(filename)
        plt.close()
    else:
        plt.show()


# 3a. Average score vs weekly self-study hours
scatter_with_trend(
    x=df["weekly_self_study_hours"],
    y=df["average_score"],
    x_label="Weekly Self-Study Hours",
    y_label="Average Score",
    title="Average Score vs Weekly Self-Study Hours",
    # filename=PROJECT_ROOT / "figures" / "scatter_study_continuous.pdf",
)

# 3b. Average score vs absence days
scatter_with_trend(
    x=df["absence_days"],
    y=df["average_score"],
    x_label="Absence Days",
    y_label="Average Score",
    title="Average Score vs Absence Days",
    # filename=PROJECT_ROOT / "figures" / "scatter_absence_continuous.pdf",
)

# -------------------------------------------------
# 4. Correlation summary
# -------------------------------------------------
corr = df[["average_score", "weekly_self_study_hours", "absence_days"]].corr()
print(corr)
