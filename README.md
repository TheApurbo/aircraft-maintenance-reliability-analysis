Aircraft Maintenance Reliability Analysis

Project Overview

This project analyzes aircraft engine degradation and predicts Remaining Useful Life (RUL) using the NASA C-MAPSS dataset.

The goal is to analyze aircraft engine sensor measurements, understand degradation patterns, and develop a machine learning model for predicting the remaining useful life of aircraft engines.

Dataset

The project uses the NASA C-MAPSS (Commercial Modular Aero-Propulsion System Simulation) dataset.

Dataset source:

https://zenodo.org/records/15346912

The analysis focuses on the FD001 subset.

The dataset is automatically downloaded and extracted during the GitHub Actions workflow.

Objectives

- Analyze aircraft engine sensor data
- Calculate Remaining Useful Life (RUL)
- Study engine degradation patterns
- Analyze sensor variability
- Develop a machine learning model for RUL prediction
- Evaluate model performance using MAE and RMSE
- Automate the analysis using GitHub Actions

Methodology

Data Processing

The NASA C-MAPSS dataset is automatically downloaded and extracted using Python.

The FD001 training dataset is loaded using Pandas.

For each engine, Remaining Useful Life is calculated as:

RUL = Maximum Operating Cycle - Current Operating Cycle

Exploratory Data Analysis

The project performs:

- RUL statistics
- Missing-value analysis
- Sensor variability analysis
- Engine degradation analysis

Sensor Analysis

The variability of the 21 sensor measurements is calculated using standard deviation.

The five most variable sensors are selected for visualization and their trends are analyzed for Engine 1.

Machine Learning

A Random Forest Regression model is used to predict Remaining Useful Life.

The model uses:

- 21 sensor measurements
- 3 operating-condition settings

An engine-wise train/test split is used so that measurements from the same engine do not appear in both training and testing datasets.

Model Performance

The Random Forest Regression model was evaluated using an engine-wise train/test split.

- MAE: 29.37 cycles
- RMSE: 43.20 cycles

These metrics represent prediction error in operating-cycle units.

Visualizations

Engine Degradation and RUL

"RUL Degradation" (outputs/rul_degradation.png)

Sensor Trends

"Sensor Trends" (outputs/sensor_trends.png)

Actual vs Predicted RUL

"Actual vs Predicted RUL" (outputs/actual_vs_predicted_rul.png)

Project Structure

- .github/workflows/main.yml — GitHub Actions workflow
- src/src/data_processing.py — Main data processing and machine learning script
- outputs/ — Generated analysis visualizations
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

The workflow automatically:

1. Checks out the repository
2. Sets up Python
3. Installs dependencies
4. Downloads the NASA C-MAPSS dataset
5. Extracts the dataset
6. Processes the FD001 training data
7. Calculates RUL
8. Performs exploratory analysis
9. Analyzes sensor variability
10. Trains the Random Forest model
11. Evaluates model performance
12. Generates visualization outputs
13. Uploads the dataset and analysis results as artifacts

Reproducibility

The analysis can be reproduced through the GitHub Actions workflow.

The workflow automatically downloads the dataset and executes the complete data-processing and machine-learning pipeline.

The generated analysis files are stored as GitHub Actions artifacts.

Results

Current model results:

- MAE: 29.37 cycles
- RMSE: 43.20 cycles

The project demonstrates an end-to-end aircraft engine reliability analysis workflow including data processing, RUL calculation, exploratory analysis, visualization, machine learning, and automated execution.

Conclusion

This project demonstrates a data-driven approach to aircraft engine reliability analysis and Remaining Useful Life prediction.

The approach can be further extended with additional C-MAPSS subsets, feature engineering, hyperparameter optimization, and advanced time-series machine learning models.
