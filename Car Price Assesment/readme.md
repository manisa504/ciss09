![image](https://cdn.shopify.com/s/files/1/0196/5170/files/Tesla-Models-Compared.jpg?v=1586714150)

[![Python](https://img.shields.io/badge/python-3.9+-blue.svg?style=flat-square)](https://www.python.org)
[![Pandas](https://img.shields.io/badge/Pandas-Data_Analysis-blue.svg?style=flat-square)](https://pandas.pydata.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Data_Visualization-blue.svg?style=flat-square)](https://seaborn.pydata.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Plotting-blue.svg?style=flat-square)](https://matplotlib.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg?style=flat-square)](https://jupyter.org/)
[![NumPy](https://img.shields.io/badge/NumPy-Data_Processing-blue.svg?style=flat-square)](https://numpy.org/)
[![SciPy](https://img.shields.io/badge/SciPy-Scientific_Computing-blue.svg?style=flat-square)](https://scipy.org/)
[![Scikit-Learn](https://img.shields.io/badge/scikit_learn-Machine_Learning-orange.svg?style=flat-square)](https://scikit-learn.org/stable/)
[![PCA](https://img.shields.io/badge/PCA-Dimensionality_Reduction-blue.svg?style=flat-square)](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html)
[![LinearRegression](https://img.shields.io/badge/Linear_Regression-Model-orange.svg?style=flat-square)](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)
[![RandomForest](https://img.shields.io/badge/Random_Forest-Regressor-green.svg?style=flat-square)](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html)
[![LabelEncoder](https://img.shields.io/badge/LabelEncoder-Data_Preprocessing-blue.svg?style=flat-square)](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html)
[![MinMaxScaler](https://img.shields.io/badge/MinMaxScaler-Data_Scaling-blue.svg?style=flat-square)](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html)
[![StandardScaler](https://img.shields.io/badge/StandardScaler-Data_Scaling-blue.svg?style=flat-square)](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html)
[![OneHotEncoder](https://img.shields.io/badge/OneHotEncoder-Categorical_Encoding-blue.svg?style=flat-square)](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html)
[![RobustScaler](https://img.shields.io/badge/RobustScaler-Data_Scaling-blue.svg?style=flat-square)](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.RobustScaler.html)
[![TrainTestSplit](https://img.shields.io/badge/Train_Test_Split-Model_Selection-orange.svg?style=flat-square)](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html)

# Car Price Prediction Project

## Overview

This repository contains code for predicting car prices using machine learning techniques. The project involves data preprocessing, scaling, dimensionality reduction using PCA, and building a Linear Regression model to predict car prices based on specific features.

## File Structure

- **`data_preprocessing.ipynb`**: Jupyter Notebook containing code for data loading, cleaning, label encoding, and scaling of numerical features.
- **`pca_model.ipynb`**: Jupyter Notebook demonstrating PCA for dimensionality reduction and building a Linear Regression model for car price prediction.
- **`README.md`**: Documentation file summarizing the project, code structure, findings, and steps involved.

## Description

### Data Preprocessing

The `data_preprocessing.ipynb` notebook includes:

- Data loading and inspection.
- Handling missing values and outlier detection.
- Label encoding categorical data to prepare for modeling.
- Scaling numerical features using various scalers.

### Dimensionality Reduction with PCA

The `pca_model.ipynb` notebook covers:

- Standardizing the data.
- Applying PCA for dimensionality reduction.
- Analyzing explained variance to determine the number of principal components.
- Building a Linear Regression model using PCA components for car price prediction.

## Model Evaluation and Findings

The evaluation metrics used are:

- **Mean Absolute Error (MAE)**: Indicates the average difference between predicted and actual car prices.
- **Mean Squared Error (MSE)**: Measures the average squared differences between predicted and actual prices.
- **R2 Score**: Represents the proportion of variance in the target variable explained by the model.

## Descriptive Statistics

The descriptive statistics performed in the data preprocessing stage include:

- Summary statistics (mean, median, min, max, standard deviation) for numerical features.
- Visualizations such as histograms, box plots, or correlation matrices to understand feature distributions and relationships.


## Conclusion and Findings

The findings from the model evaluation are as follows:

- **Mean Absolute Error (MAE)**: The model's predictions are, on average, around $2405.05 off from the actual car prices.
- **Mean Squared Error (MSE)**: The model yields an MSE of approximately 12705826.02, indicating variance in prediction errors.
- **R2 Score**: The R2 score of 0.839 suggests that around 83.9% of the variance in car prices is explained by our model, signifying a reasonably good fit.

The Linear Regression model trained using PCA components demonstrates promising performance for car price prediction. Further analysis or model enhancements could be explored based on these results.

Feel free to explore the Jupyter Notebooks (`data_preprocessing.ipynb` and `pca_model.ipynb`) for detailed implementation steps and code specifics.

