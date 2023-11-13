# Car Price Prediction Analysis

## Overview
This Python script conducts a thorough analysis of a car pricing dataset. The process includes data exploration, preprocessing, feature engineering, and model training and evaluation.

## Description
The script is structured into several key sections:

1. **Data Exploration**: Understanding the dataset through various checks and visualizations.
2. **Data Preprocessing**: Includes encoding categorical variables and scaling numerical variables.
3. **Feature Engineering**: Generation of new features and use of techniques like PCA for dimensionality reduction.
4. **Model Training and Evaluation**: Training a regression model using the processed data and evaluating its performance.

## Libraries Used
- pandas
- seaborn
- matplotlib
- sklearn

## Dataset
The dataset used is named `CarPrice_Assignment.csv`, which includes various features related to car specifications and their pricing.

## Usage
Run the script in a Python environment. Ensure all the required libraries are installed. The script is self-contained and will execute all the steps from data loading to model evaluation.

## Key Functions
- Data loading and basic checks
- Visualization of relationships between different variables
- Preprocessing steps like OneHotEncoding and StandardScaler
- PCA for feature reduction
- Training a RandomForestRegressor model
- Evaluating the model using metrics like MAE, MSE, and R2 Score

## Contributions
Feel free to fork this project and contribute. Any enhancements, particularly in the model training and feature engineering sections, are welcome.

## License
[MIT License](https://opensource.org/licenses/MIT)
