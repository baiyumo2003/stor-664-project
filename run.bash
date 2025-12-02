#!/usr/bin/env bash

# Run data loading
python3 src/01_load_data.py

# Run EDA boxplot
python3 src/02_eda_boxplot.py

# Run EDA continuum
python3 src/03_eda_continuum.py

# Run analysis testing
python3 src/04_analysis_testing.py