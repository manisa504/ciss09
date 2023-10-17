
# LinkedIn Post Summary

## Exploratory Data Analysis of Job Data and AI Impact

In a rapidly evolving technological landscape, the integration of artificial intelligence (AI) across various job sectors is becoming increasingly prevalent. To understand the depth of AI's impact on different job titles, a comprehensive exploratory data analysis was conducted on a dataset containing information about various job titles and their relationship with AI.

Please check out my EDA analysis on job_data using [this link](#).

---


# Introduction:

In today's technology-driven landscape, the impact of Artificial Intelligence (AI) on job roles across various sectors is profound. 
This project dives into a dataset that reveals the depth of AI's influence on different job titles, highlighting the potential 
risk of automation and the relationship between tasks and AI applications. Through visual explorations, the goal is to provide a 
snapshot of how AI might be reshaping the future of work across diverse domains.

```python
#import module 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv("Job_Data.csv")

# Display the first few rows of the dataset
data.head()
```

## Data Preparation:

First, we need to ensure that our dataset is clean and ready for analysis. This includes checking for missing values, examining data types, and performing necessary data conversions.

```python
# Check for missing values
missing_values = data.isnull().sum()

# Check data types of each column
data_types = data.dtypes

# Convert "AI Impact" column to numerical by removing the '%' symbol and converting to float
data['AI Impact'] = data['AI Impact'].str.rstrip('%').astype('float') / 100.0

# Check summary statistics for the numerical columns
summary_statistics = data.describe()
```

## Handling Infinite Values:

It's important to address any infinite values in the dataset, as they can distort our analysis. We'll replace them with NaN values for clarity.

```python
import numpy as np

# Replace infinite values with NaN
data['AI_Workload_Ratio'].replace([np.inf, -np.inf], np.nan, inplace=True)

# Count the number of NaN values in the 'AI_Workload_Ratio' column
nan_count = data['AI_Workload_Ratio'].isna().sum()
```

## Univariate Analysis:

Let's examine the distributions of 'AI Impact', 'Tasks', 'AI models', and the count of job titles in each 'Domain'.

```python
# ... (visualization code here)
```

## Bivariate Analysis:

We'll also explore relationships between pairs of variables. Specifically, we'll look at how 'AI Impact' relates to 'Tasks' and the correlation between 'AI models' and 'Tasks'.

```python
# ... (visualization code here)
```

## Insights:

- Distribution of AI Impact:
- ... (other insights)

## Conclusions:

- Risk of AI Automation:
- ... (other conclusions)
