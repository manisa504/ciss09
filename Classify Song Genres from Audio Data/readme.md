![image](https://github.com/manisa504/manisha/assets/97705567/bb0232b5-0788-4a3b-bf1f-bfd2f6c4f683)


[![Python](https://img.shields.io/badge/Python-3.x-blue)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data_Processing-blue.svg?style=flat-square)](https://pandas.pydata.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Data_Visualization-blue.svg?style=flat-square)](https://matplotlib.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Statistical_Data_Visualization-blue.svg?style=flat-square)](https://seaborn.pydata.org/)
[![Scikit-Learn](https://img.shields.io/badge/scikit_learn-Machine_Learning-orange.svg?style=flat-square)](https://scikit-learn.org/stable/)
[![StandardScaler](https://img.shields.io/badge/StandardScaler-Feature_Scaling-blue.svg?style=flat-square)](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html)
[![PCA](https://img.shields.io/badge/PCA-Dimensionality_Reduction-blue.svg?style=flat-square)](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html)
[![DecisionTreeClassifier](https://img.shields.io/badge/DecisionTree-Classifier-orange.svg?style=flat-square)](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html)
[![LogisticRegression](https://img.shields.io/badge/LogisticRegression-Classifier-orange.svg?style=flat-square)](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html)
[![KFold](https://img.shields.io/badge/KFold-Cross_Validation-blue.svg?style=flat-square)](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html)
[![Pipeline](https://img.shields.io/badge/Pipeline-Workflow_Orchestration-blue.svg?style=flat-square)](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html)

# Music Genre Classification Project

## Overview

This repository contains code for classifying music genres (specifically Hip-Hop and Rock) using machine learning techniques. The project involves data preprocessing, feature scaling, dimensionality reduction using PCA, and building classification models (Decision Tree Classifier, Logistic Regression) to classify music tracks into genres based on track metrics.

## File Structure

- **`data_preprocessing.ipynb`**: Jupyter Notebook containing code for data loading, preprocessing, feature scaling, and PCA.
- **`music_genre_classification.ipynb`**: Jupyter Notebook demonstrating classification models, model comparison, data balancing, and cross-validation.
- **`README.md`**: Detailed documentation summarizing the project, methods used, results, and model performance.

## Description

### Data Preprocessing

- Loaded track metadata with genre labels and track metrics.
- Merged relevant columns of track metrics and genre labels.
- Explored data information and performed correlation analysis between features.

### Feature Scaling and Normalization

- Split data into training and testing sets.
- Normalized feature data using StandardScaler to prepare for PCA.

### Principal Component Analysis (PCA)

- Utilized PCA to reduce dimensionality and find essential features.
- Determined the number of components based on explained variance ratios and cumulative explained variance plots.

### Model Building and Evaluation

- Built classification models: Decision Tree Classifier and Logistic Regression.
- Evaluated models using classification reports to assess precision, recall, and F1-score for Hip-Hop and Rock genres.

### Data Balancing and Model Bias Reduction

- Balanced dataset to address bias towards the more prevalent class (Rock).
- Evaluated models after balancing to check improvements in model performance.

### Cross-Validation for Model Evaluation

- Implemented K-Fold Cross-Validation to rigorously evaluate model performance.
- Utilized pipelines to scale, perform PCA, and train models using K-Fold CV.

## Results

### Model Performance

#### Decision Tree Classifier:

- Precision (Hip-Hop): 0.75, Precision (Rock): 0.77
- Recall (Hip-Hop): 0.79, Recall (Rock): 0.73
- F1-score (Hip-Hop): 0.77, F1-score (Rock): 0.75

#### Logistic Regression:

- Precision (Hip-Hop): 0.81, Precision (Rock): 0.83
- Recall (Hip-Hop): 0.83, Recall (Rock): 0.80
- F1-score (Hip-Hop): 0.82, F1-score (Rock): 0.82

### Conclusion

- Both models show promising performance after balancing the dataset.
- Logistic Regression slightly outperforms the Decision Tree Classifier.
- K-Fold Cross-Validation confirms the stability of models with mean scores of approximately 72% and 77% for Decision Tree and Logistic Regression, respectively.

The project demonstrates effective classification of music genres using machine learning techniques, with Logistic Regression showing slightly better performance compared to Decision Tree Classifier.

