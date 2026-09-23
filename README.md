Aircraft Maintenance Reliability Analysis

Project Overview

This project analyzes aircraft engine degradation and predicts Remaining Useful Life (RUL) using the NASA C-MAPSS dataset.

The goal is to analyze aircraft engine sensor measurements, understand degradation patterns, and develop a machine learning model for predicting the remaining useful life of aircraft engines.

Dataset

The project uses the NASA C-MAPSS (Commercial Modular Aero-Propulsion System Simulation) dataset.

Dataset source:

https://zenodo.org/records/15346912

The analysis focuses on the FD001 subset.

The dataset is automatically downloaded and extracted during the GitHub Actions workflow, so the raw dataset does not need to be stored directly in the repository.

Objectives

- Analyze aircraft engine sensor data
- Calculate Remaining Useful Life (RUL)
- Study engine degradation patterns
- Analyze sensor variability
- Develop a machine learning model for RUL prediction
- Evaluate model performance using MAE and RMSE
- Automate the analysis using GitHub Actions

Methodology

1. Data Processing

The NASA C-MAPSS dataset is automatically downloaded and extracted using Python.

The FD001 training dataset is loaded using Pandas.

For each engine, Remaining Useful Life is calculated as:

RUL = Maximum Operating Cycle - Current Operating Cycle

2. Exploratory Data Analysis

The project performs basic exploratory analysis including:

- Number of engines
- Operating cycles
- RUL statistics
- Missing-value analysis
- Sensor variability analysis
- Engine degradation patterns

3. Sensor Analysis

The variability of the 21 sensor measurements is calculated using standard deviation.

The five most variable sensors are selected for visualization and their trends are analyzed for Engine 1.

4. Machine Learning

A Random Forest Regression model is used to predict Remaining Useful Life.

The model uses:

- 21 sensor measurements
- 3 operating-condition settings

An engine-wise train/test split is used so that measurements from the same engine do not appear in both the training and testing datasets.

This helps reduce data leakage between training and testing data.

Model Performance

The Random Forest Regression model was evaluated using an engine-wise train/test split.

- Mean Absolute Error (MAE): 29.37 cycles
- Root Mean Squared Error (RMSE): 43.20 cycles

These metrics represent prediction error in operating-cycle units.

Visualizations

The project generates the following analysis outputs:

- Engine degradation and RUL trends
- Sensor trends for the most variable sensors
- Actual versus predicted RUL

The generated visualization files are available through the GitHub Actions Analysis-Results artifact.

Project Structure

- .github/workflows/main.yml — GitHub Actions workflow
- src/src/data_processing.py — Main data processing and machine learning script
- README.md — Project documentation
- requirements.txt — Python dependencies

Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- GitHub Actions

GitHub Actions Workflow

The project uses GitHub Actions to automate the complete analysis pipeline.

The workflow automatically:

1. Checks out the repository
2. Sets up Python
3. Installs project dependencies
4. Downloads the NASA C-MAPSS dataset
5. Extracts the dataset
6. Processes the FD001 training data
7. Calculates Remaining Useful Life
8. Performs exploratory analysis
9. Analyzes sensor variability
10. Trains the Random Forest model
11. Evaluates model performance
12. Generates visualization outputs
13. Uploads the dataset and analysis results as workflow artifacts

Reproducibility

The analysis can be reproduced through the GitHub Actions workflow.

The workflow automatically downloads the dataset and executes the complete data-processing and machine-learning pipeline.

The generated analysis files are stored as GitHub Actions artifacts.

Results

The current Random Forest model produces the following evaluation results:

- MAE: 29.37 cycles
- RMSE: 43.20 cycles

The project successfully demonstrates an end-to-end aircraft engine reliability analysis workflow, including data processing, RUL calculation, exploratory analysis, visualization, machine learning, and automated execution.

Conclusion

This project demonstrates a data-driven approach to aircraft engine reliability analysis and Remaining Useful Life prediction.

By combining sensor data analysis, degradation visualization, machine learning, and automated GitHub Actions workflows, the project provides a reproducible framework for predictive maintenance research.

The approach can be further extended with additional C-MAPSS subsets, feature engineering, hyperparameter optimization, and advanced time-series machine learning models.
