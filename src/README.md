# Source Code Folder (`/src`)

This folder contains all scripts used in the project.

## Structure

```
src/
├── 01_load_data.py        # Data import and cleaning
├── 02_eda_boxplot.py      # Exploratory Data Analysis using boxplots
├── 03_eda_continuum.py    # Additional EDA focusing on continuum analysis
├── 04_analysis_testing.py # Final analysis and testing scripts
```

## Script Responsibilities

### **01_load_data.py**

* Reads raw data files.
* Cleans and preprocesses data.
* Saves cleaned datasets to the `data/` or `results/` directory.

### **02_eda_boxplot.py**

* Conducts exploratory data analysis using boxplots.
* Generates visual summaries and descriptive statistics.
* Saves figures to the `results/` directory.

### **03_eda_continuum.py**

* Performs additional EDA focused on continuum-related insights.
* Produces plots or summary tables.
* Outputs saved to `results/`.

### **04_analysis_testing.py**

* Runs final analyses, model testing, or evaluation procedures.
* Produces tables, figures, or summaries stored in `results/`.

