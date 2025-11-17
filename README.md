
# stor-664-project-sample

## Team Members
- Suhan Liu(@suhanliu)
- Yumo Bai(@baiyumo2003)
- Beichen Wan(@wanbch3)
- Xu Huang(@XuHuang38)

## Overview
This repository contains the group project for [STOR 664, Fall 2025].  
Our goal is to ... using data ... and methods ....
Results show ...

## Repository Structure
| Folder | Purpose | Key Files |
|---------|----------|-----------|
| `/data/raw` | Original unmodified datasets | `student-scores.csv`, `data2.csv` |
| `/data/processed` | Cleaned datasets ready for analysis | `student_scores_clean.csv` |
| `/src` | Analysis and visualization code | `01_load_data.py` |
| `/results/tables` | Numeric summaries |  |
| `/results/figures` | Visual outputs |  |
| `/report` | All written deliverables | |

## Getting Started
### 1. Clone the repository

```bash
git clone baiyumo2003/stor-664-project
cd stor-664-project
```

### 2. Install dependencies (optional but highly recommended)
Example in Python:
```python
pip install -r requirements.txt
```

### 3. Running Analysis Scripts
```r
Rscript scripts/03_generate_figures.R
```

---

## Contributing

1) Create a feature branch for each component of the project. For example, for the methods deliverable:
```bash
git checkout -b methods
```

2) Every team member should be working on this branch for the methods component of the project.
   - Use concise, meaningful messages:
     ```
     git commit -m "Add OLS model fitting script"
     ```
4) Before the submission deadline, open a PR and set Dr. Kessler and Shaleni as reviewers. If this is a peer reviwed component, make sure your reviewer(s) have access to the repository and are also assigned as reviewers on the PR. A link to your PR will need to be included as part of your Gradescope submission.
5) Incorporate feedback as necessary, update the feature branch, and close the PR before moving to the next component.
   - Your next feature branch should be created from your newly updated `main` branch.
   - `main` should only be updated from one of the feature branches after a PR.

## Peer Reviewing

For one component of the project you will be asked to peer-review another team's pull request. When doing so, make sure to leave **at least two** constructive comments. You will be asked to provide links to your two comments in Gradescope.

Your peer reviewers should be able to clone and run your repository to reproduce your results.

## Reports

Any medium can be used to generate the reports (MS Word, Latex, Quarto etc), however the final result will need to be a PDF file that will be placed in the `\reports` folder as well as uploaded on Gradescope.
