![image](https://s.yimg.com/ny/api/res/1.2/Yq7MYGRuWyV7U7xYt3Eyig--/YXBwaWQ9aGlnaGxhbmRlcjt3PTY0MDtoPTQyNw--/https://media.zenfs.com/en/reuters-finance.com/ab8f6d95ba09e93690e6a2e2bb873b98)
# Banking Recovery Analysis

This README provides an extensive overview of the analysis conducted on banking recovery strategies, focusing on regression discontinuity. The analysis aims to assess whether the incremental recovery at higher strategy levels exceeds the additional cost incurred by the bank ($50 per customer). The steps and findings are outlined below:

## Introduction
After a debt is declared "uncollectable," banks attempt to recover a portion of the owed amount. The recovery strategies vary based on different expected recovery thresholds ($1000, $2000, etc.), with higher thresholds implying increased effort and cost in contacting customers.

## Steps of Analysis

### 1. Data Loading and Overview
- Imported required modules: Pandas and NumPy.
- Loaded the banking dataset ('bank_data.csv') into a Pandas DataFrame named 'df'.
- Displayed the initial rows of the dataset to understand its structure and contents.

### 2. Graphical Exploratory Data Analysis
- Explored recovery strategies at different thresholds ($1000 and $2000).
- Plotted a scatter plot of age against expected recovery amount to identify potential discontinuities.

### 3. Statistical Test: Age vs. Expected Recovery Amount
- Utilized the Kruskal-Wallis test to analyze the average age above and below the $1000 threshold.
- Concluded that age did not significantly differ around the threshold.

### 4. Statistical Test: Sex vs. Expected Recovery Amount
- Examined the percentage of male customers above and below the $1000 threshold using chi-square tests.
- Results indicated no substantial change in gender percentages around the threshold.

### 5. Exploratory Graphical Analysis: Recovery Amount
- Developed scatter plots of expected recovery amount vs. actual recovery amount around the $1000 threshold.
- Sought discontinuities in recovery amounts before and after the threshold.

### 6. Statistical Analysis: Recovery Amount
- Conducted Kruskal-Wallis tests to examine discontinuities in actual recovery amounts around the $1000 threshold.
- Obtained statistically significant results indicating a jump in recovery amounts.

### 7. Regression Modeling: No Threshold
- Built a linear regression model to predict actual recovery amount based on expected recovery amount.
- Evaluated the relationship between these variables and estimated the variance explained by the model.

### 8. Regression Modeling: Adding True Threshold
- Created an indicator variable for the true threshold ($1000) and included it in the regression model.
- Analyzed the impact of the higher recovery strategy above and below the threshold.

### 9. Regression Modeling: Adjusting the Window
- Repeated the analysis with a narrower window ($950 to $1050) to validate the findings.
- Confirmed that the higher recovery strategy yields a substantial increment in recovery amounts compared to the additional cost per customer.

## Steps of Analysis

(Sections 1-6 are detailed descriptions of the steps of the analysis.)

### Results Overview
The analysis provided a multi-faceted examination of banking recovery strategies, focusing on the impact of higher recovery levels above and below the $1000 threshold.

- **Graphical Exploratory Data Analysis:** Visual inspection of scatter plots suggested potential discontinuities in age and actual recovery amounts around the $1000 threshold.
- **Statistical Tests:** Employed Kruskal-Wallis tests and chi-square tests to assess age, sex, and actual recovery amounts above and below the threshold.
- **Regression Modeling:** Utilized linear regression models to estimate the relationship between expected and actual recovery amounts, including models with and without the true threshold indicator.

### Key Findings
1. **Age and Sex Analysis:** No significant jump or difference was observed in the average age or percentage of male customers around the $1000 threshold, indicating consistency in these demographics above and below the threshold.
2. **Actual Recovery Amounts:** Statistical tests revealed a significant discontinuity in actual recovery amounts at the $1000 threshold, indicating a substantial increase in recovery amounts beyond this level.

### Conclusion
The analysis consistently demonstrated that implementing a higher recovery strategy beyond the $1000 threshold resulted in a substantial increase in actual recovery amounts. This observed increase in recovered amounts was found to exceed the additional cost of $50 per customer required for the higher strategy.

Through a meticulous exploration involving various statistical tests, graphical analyses, and regression models, the findings consistently underscored the positive impact of the higher recovery strategy. Consequently, the comprehensive analysis supports the effectiveness of the higher recovery strategy in generating greater recoveries compared to the incremental costs incurred.

The robust findings from multiple methodologies suggest that the bank's decision to employ a more intensive recovery strategy for amounts exceeding $1000 is justified. The analysis convincingly showcased that the higher recovery strategy, implemented beyond the $1000 threshold, significantly amplified the recovery amount, surpassing the additional cost per customer ($50).

This conclusion stems from the comprehensive evaluation of statistical tests, exploratory data analysis, and regression modeling, ensuring a thorough and dependable assessment of the data.

The README offers an extensive overview of the complete analysis, delineating the steps undertaken, the array of statistical tests performed, and the compelling conclusions derived from the data analysis process.

