import pandas as pd
import numpy as np
from pathlib import Path

import statsmodels.api as sm
import statsmodels.formula.api as smf

# -------------------------------------------------
# 1. Load data
# -------------------------------------------------

# Project root = parent of the src folder where this file lives
PROJECT_ROOT = Path(__file__).resolve().parents[1]

# Path to the processed data file
data_path = PROJECT_ROOT / "data" / "processed" / "student_scores_clean.csv"

df = pd.read_csv(data_path)

# -------------------------------------------------
# 2. Construct outcome: average score across subjects
# -------------------------------------------------

score_cols = [
    "math_score",
    "history_score",
    "physics_score",
    "chemistry_score",
    "biology_score",
    "english_score",
    "geography_score",
]

df["average_score"] = df[score_cols].mean(axis=1)

# -------------------------------------------------
# 3. Prepare predictors and controls
# -------------------------------------------------
# Key predictors for the three null hypotheses:
#   - weekly_self_study_hours
#   - absence_days
#   - extracurricular_activities (participation)
#
# We also include a few controls to reflect the
# "holding other variables fixed" language:
#   - gender
#   - part_time_job
#   - career_aspiration

# Make an explicit 0/1 variable for extracurricular participation
df["extra_participation"] = df["extracurricular_activities"].astype(int)

# -------------------------------------------------
# 4. Fit multiple linear regression model
# -------------------------------------------------
# Model:
#   average_score ~ weekly_self_study_hours
#                   + absence_days
#                   + extra_participation
#                   + gender (categorical)
#                   + part_time_job (categorical)
#                   + career_aspiration (categorical)

formula = (
    "average_score ~ "
    "weekly_self_study_hours + "
    "absence_days + "
    "extra_participation + "
    "C(gender) + "
    "C(part_time_job) + "
    "C(career_aspiration)"
)

model = smf.ols(formula=formula, data=df).fit()

# Print full regression summary (coefficients, t-stats, p-values, etc.)
print(model.summary())

# -------------------------------------------------
# 5. Formal tests of the three null hypotheses
# -------------------------------------------------
# H0,1: self-study hours are not associated with average score
#       <=> coefficient on weekly_self_study_hours = 0
#
# H0,2: absence days are not associated with average score
#       <=> coefficient on absence_days = 0
#
# H0,3: extracurricular participation is not associated with average score
#       <=> coefficient on extra_participation = 0

# Each of these is a standard t-test on a single coefficient.

test_study = model.t_test("weekly_self_study_hours = 0")
test_absence = model.t_test("absence_days = 0")
test_extra = model.t_test("extra_participation = 0")

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

# -------------------------------------------------
# 6.Joint test of all three coefficients
# -------------------------------------------------
# If you also want to test the joint null that all three
# key predictors have no effect:
#   H0_all: weekly_self_study_hours = 0,
#           absence_days = 0,
#           extra_participation = 0

test_joint = model.f_test([
    "weekly_self_study_hours = 0",
    "absence_days = 0",
    "extra_participation = 0",
])

print("\n========================================")
print("Joint test of all three predictors (optional)")
print("========================================")
print(test_joint)
