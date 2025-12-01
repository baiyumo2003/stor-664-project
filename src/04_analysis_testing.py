import pandas as pd
import numpy as np
from pathlib import Path

import statsmodels.api as sm
import statsmodels.formula.api as smf


PROJECT_ROOT = Path(__file__).resolve().parents[1]

# Path to the processed data file
data_path = PROJECT_ROOT / "data" / "processed" / "student_scores_clean.csv"

df = pd.read_csv(data_path)


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


df["extra_participation"] = df["extracurricular_activities"].astype(int)



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

print(model.summary())


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


test_joint = model.f_test([
    "weekly_self_study_hours = 0",
    "absence_days = 0",
    "extra_participation = 0",
])


print("\n========================================")
print("Joint test of all three predictors (optional)")
print("========================================")
print(test_joint)
