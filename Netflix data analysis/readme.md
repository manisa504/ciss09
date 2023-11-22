![image](https://images.ctfassets.net/4cd45et68cgf/7ciNwxNKBqygzOsGzp1jSI/1d13387defe2332403543d610a10b1cc/-_____________________--__________________-____________________________________2022_________________________________________.jpg?w=2560)
# Netflix Movie Duration Analysis

## Introduction
Netflix, the streaming giant, offers a vast library of movies and series. This project revolves around analyzing movie duration trends over the years. The goal is to determine if there's evidence supporting the assertion that the average duration of movies has been declining. The analysis involves utilizing Python and pandas to work with the provided data and visualize the trends.

## Loading and Analyzing Provided Data
### 1. Loading Movie Duration Data
The analysis begins with a provided set of movie duration averages for each year from 2011 to 2020.

### 2. Creating a DataFrame
Using Python dictionaries and pandas, a DataFrame is created with movie duration averages for respective years. This DataFrame is then inspected to ensure the correct creation of data structures.

### 3. Visualizing Movie Duration Trends
A line plot is generated to visualize the trends in movie durations from 2011 to 2020. The x-axis represents years, and the y-axis represents average movie durations.

## Exploring the Full Dataset
### 4. Loading the Complete Netflix Dataset
The full Netflix dataset is accessed from a CSV file provided at the path "datasets/netflix_data.csv". The DataFrame generated from this dataset includes multiple columns like show_id, type, title, director, cast, country, release_year, duration, description, and genre.

### 5. Filtering for Movies
A new DataFrame is created, focusing solely on movies by filtering rows where the type is "Movie". Columns of interest, including title, country, genre, release_year, and duration, are extracted for further analysis.

### 6. Visualizing Movie Duration by Release Year
A scatter plot is created to visualize movie duration by release year. This plot highlights the distribution of movie durations over time, displaying the release year on the x-axis and movie duration on the y-axis.

## Analyzing Specific Movie Durations
### 7. Exploring Short Movie Durations
Movies with durations shorter than 60 minutes are extracted for analysis. These movies are displayed in a DataFrame to inspect their titles, countries, genres, release years, and durations.
Trend in Movie Durations: Visual analysis from 2011 to 2020 suggests a potential decline in average movie durations over the years. The line plot shows a gradual decrease in average movie durations during this period.

Exploration of Complete Dataset:

Data Loading: The complete Netflix dataset was accessed, containing various attributes such as type, title, country, genre, release year, and duration.
Focus on Movies: Filtering the dataset for movies allowed a more detailed examination of movie-related attributes.
Visualizing Movie Duration by Release Year:

A scatter plot was created to represent movie durations across different release years.
This visualization highlighted trends in movie durations, showcasing the distribution and density of movie lengths over time.
Analysis of Specific Movie Durations:

Short Movie Durations: Movies with durations under 60 minutes were identified.
Non-Feature Films: Shorter durations were often linked to genres like children's movies, documentaries, and stand-up specials.
Enhanced Scatter Plot:

Different colors were utilized to distinguish non-typical genres on the scatter plot, aiding in identifying their impact on movie durations.
### 8. Identifying Non-Feature Films
The short movie durations mostly correspond to genres like "Children", "Documentaries", and "Stand-Up". These genres are distinct and often tend to have shorter durations compared to typical feature films.

### 9. Plotting Genres with Different Colors
A loop generates a list of colors based on the genre of movies, allowing the differentiation of non-typical genres on the scatter plot.

### 10. Enhanced Scatter Plot
The scatter plot of movie durations by release year is enhanced with different colors indicating non-typical genres. Axis labels and a specific style are applied for visual clarity and appeal.

## Conclusion
The analysis explores trends in movie durations and identifies that shorter durations are often associated with specific genres such as children's movies, documentaries, and stand-up specials. While these genres contribute to shorter movie durations, the analysis does not definitively prove a general decline in movie durations.

## Next Steps
Further analysis is required to understand the underlying factors contributing to movie durations. Exploring genre-specific trends, identifying outliers, and conducting statistical analyses could provide deeper insights into changes in movie lengths over time.
