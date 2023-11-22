![image](https://www.finereport.com/en/wp-content/uploads/2020/06/2020062201I-1024x576.png)
# Sales Analysis

This repository contains a Python script that conducts an analysis on sales data, cleans it, and derives insights from it using the Pandas library.

## Overview

The script is structured in multiple sections that perform different operations on sales data:

### Merging Sales Data

The script starts by merging 12 months of sales data into a single CSV file using the Pandas `concat` function.

### Data Cleaning

- Removes rows with missing or NaN values in the dataset.
- Deletes specific erroneous data entries, such as entries containing 'Or' in the 'Order Date' column.
- Converts columns to their appropriate data types (e.g., numeric columns converted to integers or floats).

### Data Augmentation

- Adds columns to the dataset to enhance analysis, such as extracting the 'Month' from the 'Order Date' column and calculating the 'Sales' column by multiplying 'Quantity Ordered' and 'Price Each'.
- Derives a new 'City' column based on the 'Purchase Address' to analyze sales data based on city.

### Sales Analysis

- Analyzes sales performance by month to identify the best-performing month in terms of revenue.
- Identifies the city with the highest sales.

### Time Analysis

- Determines the best time to display advertisements to maximize the likelihood of customers making a purchase.

### Product Analysis

- Analyzes frequently sold products together by identifying pairs of products that are often ordered together.
- Visualizes the quantity ordered and price of each product using bar and line graphs.

## Usage

1. Ensure Python and necessary libraries (Pandas, Matplotlib) are installed.
2. Run the script in a Python environment.
3. Follow the prompts in the script to load and analyze sales data.

## File Structure

- `sales_analysis.py`: Python script for sales data analysis.

## Notes

- The script may contain warnings or errors related to setting values on slices of a DataFrame. Consider revising the code for better handling of DataFrame slices.
- It uses Pandas, Matplotlib libraries for data manipulation and visualization, respectively.

Feel free to explore, modify, or enhance the script according to your requirements!
