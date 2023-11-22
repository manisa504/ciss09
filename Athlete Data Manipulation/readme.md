![image](https://d2r55xnwy6nx47.cloudfront.net/uploads/2019/04/Bolt_2880x1620_Lede.jpg)
# Athlete Dataset Analysis

## Overview
This analysis is performed on the 'Athlete' dataset, involving data manipulation using Pandas and NumPy libraries in Python. The dataset contains information about athletes' ID, age, height, weight, and year.

## Analysis Steps

### 1. Importing and Displaying the Data
- Imported Pandas and NumPy libraries to perform data operations.
- Loaded the 'Athlete.csv' file into a Pandas DataFrame named 'my_data'.
- Displayed the first 5 rows of the dataset using `my_data.head()`.

### 2. Creating a NumPy Array
- Converted the DataFrame 'my_data' into a NumPy array named 'my_list'.
- Checked the shape of the NumPy array, which resulted in dimensions (27, 5).

### 3. Deducting Weight and Modifying Year
- Deducted 10 from all athletes' weights and stored the new values in a new column named 'new_Weight'.
- Overwrote the 'Year' value of the 2nd row with 1993 where the athlete's ID is 1.
- Displayed the 'Year' column to verify changes made.

### 4. Calculating Weight-to-Height Ratio
- Added a new column 'wt_ht' to the DataFrame to represent the ratio of weight to height for each athlete.
- Calculated the ratio using the modified weight values and the original height values.

## Conclusion
The analysis involved initial data import, conversion, and manipulation using Pandas and NumPy libraries. It included operations like displaying data, array creation, data modification, and ratio calculation, providing insights into athletes' characteristics and alterations made to the dataset.
