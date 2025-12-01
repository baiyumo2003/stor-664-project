import pandas as pd
import numpy as np
from pathlib import Path

import statsmodels.api as sm
import statsmodels.formula.api as smf


PROJECT_ROOT = Path(__file__).resolve().parents[1]

# Path to the processed data file
data_path = PROJECT_ROOT / "data" / "processed" / "student_scores_clean.csv"

df = pd.read_csv(data_path)

# --------------------------
# Construct average score
# --------------------------
score_cols = [
    "math_score", "history_score", "physics_score",
    "chemistry_score", "biology_score",
    "english_score", "geography_score"
]

df["average_score"] = df[score_cols].mean(axis=1)

df["extra_participation"] = df["extracurricular_activities"].astype(int)

df["part_time_job"] = df["part_time_job"].astype(int)

cutoff = 3
df["absence_over_cutoff"] = np.where(df["absence_days"] > cutoff,
                                     df["absence_days"] - cutoff,
                                     0)

# -------------------------------------
# Interaction term:
# absenteeism × study hours
# -------------------------------------
df["absence_study_interaction"] = (
    df["absence_over_cutoff"] * df["weekly_self_study_hours"]
)

# -------------------------------------
# Regression model with interaction
# and optional nonlinear absenteeism
# -------------------------------------
formula = (
    "average_score ~ "
    "weekly_self_study_hours + "
    "absence_days + "
    "absence_over_cutoff + "
    "absence_study_interaction + "
    "extra_participation + "
    "part_time_job + "
    "C(gender) + "
    "C(career_aspiration)"
)

model = smf.ols(formula=formula, data=df).fit()
print(model.summary())

# -----------------------------
# Individual t-tests
# -----------------------------
test_study = model.t_test("weekly_self_study_hours = 0")
test_absence = model.t_test("absence_days = 0")
test_extra = model.t_test("extra_participation = 0")
test_interaction = model.t_test("absence_study_interaction = 0")

print("\n========================================")
print("Test for H0,1: Effect of self-study hours")
print("========================================")
print(test_study)

print("\n========================================")
print("Test for H0,2: Effect of absence days")
print("========================================")
print(test_absence)

print("\n========================================")
print("Test for H0,3: Effect of extracurricular participation")
print("========================================")
print(test_extra)

print("\n========================================")
print("Test for H0,4: Interaction effect (absence_cutoff × study hours)")
print("========================================")
print(test_interaction)

# ------------------------------------------
# Joint F-test of core predictors
# ------------------------------------------
test_joint = model.f_test([
    "weekly_self_study_hours = 0",
    "absence_days = 0",
    "extra_participation = 0",
])

print("\n========================================")
print("Joint test of three predictors")
print("========================================")
print(test_joint)
