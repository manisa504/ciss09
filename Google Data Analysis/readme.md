![image](https://techcrunch.com/wp-content/uploads/2022/03/GettyImages-1235737290.jpeg?w=1024)
# Google Play Store Apps and Reviews Analysis

This repository contains a comprehensive analysis of over ten thousand Android apps in the Google Play Store across different categories. The analysis includes insights derived from two main datasets: `apps.csv` (details of the applications on Google Play) and `user_reviews.csv` (containing reviews for each app).

## Objective

The primary objective of this analysis was to gain insights into the Android app market, identify trends, and devise strategies for growth and retention by leveraging data analytics.

## Key Findings

### 1. Data Cleaning and Correcting Data Types

- Removed special characters from 'Installs' and 'Price' columns to make them numeric.
- Corrected data types to ensure 'Installs' and 'Price' columns contain numerical values.

### 2. App Categories Analysis

- Identified 33 unique app categories with Family and Game apps dominating the market.
- Explored the prevalence of each category to understand market distribution.

### 3. App Ratings Distribution

- Discovered an average app rating of 4.17 across all categories.
- Noted that the majority of apps received high ratings, skewing the histogram to the left.

### 4. Size and Price Analysis

- Analyzed the relationship between app size, price, and ratings.
- Found that highly rated apps generally ranged between 2 MB to 20 MB in size and were priced under $10.

### 5. App Category vs. Price Relation

- Investigated the pricing trend across different app categories.
- Observed that Medical and Family apps tend to be the most expensive.

### 6. Filtering "Junk" Apps

- Identified and filtered out "junk" apps priced above $100 to refine the analysis.

### 7. Popularity of Paid vs. Free Apps

- Explored the number of downloads for paid and free apps.
- Noticed that free apps have higher installation numbers compared to paid apps.

### 8. Sentiment Analysis of User Reviews

- Conducted sentiment analysis on user reviews to determine the mood (positive, negative, neutral).
- Found that free apps tend to receive more negative comments compared to paid apps.

## Conclusion

This analysis provides valuable insights for understanding the Google Play Store app ecosystem, including the impact of ratings, pricing strategies, user sentiment, and the distribution of apps across categories. The findings can be used for informed decision-making in app development and marketing strategies.

