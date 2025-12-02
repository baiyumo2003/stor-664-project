
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

| Path               | Purpose                                              | Key Files                                                                               |
| ------------------ | ---------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `/`                | Top-level project directory                          | `README.md`, `run.bash`, `requirements.txt`                                             |
| `/data/raw`        | Original unmodified datasets                         | `student-scores.csv`                                                                    |
| `/data/processed`  | Cleaned datasets ready for analysis                  | `student_scores_clean.csv`                                                              |
| `/src`             | Analysis and visualization code                      | `01_load_data.py`, `02_eda_boxplot.py`, `03_eda_continuum.py`, `04_analysis_testing.py` |
| `/results`         | Plots and visualizations                             | *(auto-generated)*                                                                      |
| `/report`          | Written deliverables, including final project report | *(in progress)*                                                                         |

## Running the Project

### Using `run.bash`

The repository includes a `run.bash` script to streamline execution of the full analysis pipeline.

**Usage:**

```bash
bash run.bash
```

This script typically:

* Creates necessary folders
* Runs all scripts in `/src` in order
* Generates outputs in `/results`

Make sure you have execution permissions:

```bash
chmod +x run.bash
```

## Requirements

All Python dependencies are listed in `requirements.txt`.

**To install:**

```bash
pip install -r requirements.txt
```


All code in `/src` is written in Python and structured for reproducibility. Outputs from each stage (cleaned datasets, figures, and tables) are saved into the corresponding `/results` subdirectories.


