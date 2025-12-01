
# stor-664-project
## Team Members
- Suhan Liu(@suhanliu)
- Yumo Bai(@baiyumo2003)
- Beichen Wan(@wanbch3)
- Xu Huang(@XuHuang38)

## Overview
This repository contains the group project for STOR 664 (Fall 2025). We study how high school students’ academic performance relates to their study behavior and class attendance. Using a dataset of exam scores across multiple subjects together with information on weekly self-study hours, number of absences, and extracurricular participation, we aim to quantify how each of these behaviors is associated with overall and subject-specific performance.

Our analysis is based primarily on multiple linear regression and related regression diagnostics. We begin with data cleaning and exploratory data analysis to understand basic patterns in exam scores and predictors, then fit a series of regression models for average exam score and for individual subjects. Along the way, we assess model assumptions, check for multicollinearity, and compare alternative model specifications (for example, adding interaction terms or additional control variables).

The repository includes all code used for data processing, visualization, and modeling (written in python), as well as the final project report. As we refine our models, we will update this repository with our main empirical findings and interpretation, highlighting which aspects of student behavior appear most strongly related to academic performance

## Repository Structure
| Folder | Purpose | Key Files |
|---------|----------|-----------|
| `/data/raw` | Original unmodified datasets | `student-scores.csv`|
| `/data/processed` | Cleaned datasets ready for analysis | `student_scores_clean.csv` |
| `/src` | Analysis and visualization code | `01_load_data.py` |
| `/results/tables` | Numeric summaries |  |
| `/results/figures` | Visual outputs |  |
| `/report` | All written deliverables | |

## Getting Started
### 1. Clone the repository

```bash
git clone baiyumo2003/stor-664-project.git
cd stor-664-project
```

### 2. Install dependencies (optional but highly recommended)
Example in Python:
```python
pip install -r requirements.txt
```

### 3. Running Analysis Scripts

---


