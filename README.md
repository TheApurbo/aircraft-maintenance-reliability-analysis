# Aircraft Maintenance Reliability Analysis

## Project Overview

This project analyzes aircraft engine degradation and predicts Remaining Useful Life (RUL) using the NASA C-MAPSS dataset.

The goal is to use sensor measurements and operating conditions to understand engine degradation and develop a machine learning model for RUL prediction.

## Dataset

The project uses the NASA C-MAPSS (Commercial Modular Aero-Propulsion System Simulation) dataset.

Dataset source:
Zenodo mirror of the NASA C-MAPSS dataset:
https://zenodo.org/records/15346912

The analysis focuses on the FD001 subset.

## Objectives

- Analyze aircraft engine sensor data
- Calculate Remaining Useful Life (RUL)
- Study engine degradation patterns
- Identify variable sensor measurements
- Develop a machine learning model for RUL prediction
- Evaluate model performance using MAE and RMSE

## Methodology

### 1. Data Processing

The dataset is downloaded and extracted automatically using Python.

The training data is loaded using Pandas and the RUL of each engine cycle is calculated from the maximum operating cycle of each engine.

### 2. Exploratory Analysis

The project analyzes:

- Number of engines
- Operating cycles
- RUL distribution
- Missing values
- Sensor variability

### 3. Visualization

The project generates:

- Engine degradation and RUL trend
- Sensor trend analysis
- Actual vs Predicted RUL

### 4. Machine Learning

A Random Forest Regression model is used to predict Remaining Useful Life.

The dataset is divided into training and testing sets.

Model evaluation metrics:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)

## Project Structure

```text
aircraft-maintenance-reliability-analysis/
│
├── .github/
│   └── workflows/
│       └── main.yml
│
├── src/
│   └── src/
│       └── data_processing.py
│
├── README.md
└── requirements.txt



Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- GitHub Actions

Results

The machine learning workflow successfully processes the NASA C-MAPSS FD001 dataset and produces Remaining Useful Life (RUL) predictions.

Model Performance

A Random Forest Regression model was evaluated using an engine-wise train/test split to reduce data leakage between training and testing engines.

- Mean Absolute Error (MAE): 29.37 cycles
- Root Mean Squared Error (RMSE): 43.20 cycles

The model was trained using sensor measurements and operating conditions to predict the Remaining Useful Life (RUL) of aircraft engines.
The project also generates visual outputs for:

- Engine degradation and RUL trends
- Sensor behavior
- Actual versus predicted RUL

Analysis outputs are stored as GitHub Actions artifacts for reproducibility.

Reproducibility

The GitHub Actions workflow automatically:

1. Downloads the dataset
2. Extracts the dataset
3. Processes the training data
4. Calculates RUL
5. Performs exploratory analysis
6. Trains the Random Forest model
7. Generates analysis graphs
8. Uploads the results as artifacts

Conclusion

This project demonstrates a complete workflow for aircraft engine reliability analysis and Remaining Useful Life prediction using sensor data and machine learning.

The approach provides a data-driven framework for analyzing engine degradation and estimating remaining useful life, which can support predictive maintenance research.
