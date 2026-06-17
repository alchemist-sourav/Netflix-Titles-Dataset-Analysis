# Netflix Content Analysis and Trend Prediction

## Table of Contents
1.  [Introduction](#introduction)
2.  [Data Source](#data-source)
3.  [Setup](#setup)
4.  [Data Cleaning and Preparation](#data-cleaning-and-preparation)
5.  [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
6.  [Predictive Modeling](#predictive-modeling)
7.  [Key Findings](#key-findings)
8.  [Conclusion](#conclusion)

## 1. Introduction
This notebook performs an in-depth analysis of the Netflix content catalog. It covers data loading, cleaning, exploratory data analysis to understand trends and distributions, and a basic predictive model to forecast future content releases.

## 2. Data Source
The dataset used for this analysis is `netflix_titles.csv`, which contains information about movies and TV shows available on Netflix, including details like title, director, cast, country, date added, release year, rating, duration, listed genres, and description.

## 3. Setup
Essential libraries such as `pandas` for data manipulation, `matplotlib.pyplot` and `seaborn` for visualization, and `sklearn.linear_model` for predictive modeling are imported.

## 4. Data Cleaning and Preparation
The following steps were performed to clean and prepare the data:
- The `date_added` column was converted to datetime objects, coercing errors.
- Missing values in `director`, `cast`, and `country` columns were filled with 'Unknown'.
- New features were engineered:
    - `release_decade`: Categorizes content by the decade of its release year.
    - `is_movie`: A binary flag indicating whether the content is a movie (1) or a TV show (0).
    - `content_type`: A direct copy of the `type` column.
    - `added_year`: Extracts the year from the `date_added` column.
- The `country` and `listed_in` columns, which contained comma-separated values, were processed to allow for individual analysis of countries and genres.

## 5. Exploratory Data Analysis (EDA)
EDA was conducted to understand the data's characteristics:
- **Movie vs TV Show Distribution**: A pie chart visualizes the proportion of movies versus TV shows on Netflix.
- **Content Released Per Year**: A line plot shows the trend of content releases over the years.
- **Top 10 Genres**: A bar chart displays the most popular genres.
- **Top 10 Countries by Content Volume**: A bar chart highlights countries with the highest number of titles.
- **Content by Release Decade**: A countplot illustrates the distribution of content releases across different decades.
- **Country Content Volume Heatmap**: A heatmap visualizes the top 10 countries by content volume.

## 6. Predictive Modeling
A simple linear regression model was used to predict future content releases:
- The `yearly_content` DataFrame, which contains the count of releases per year, was used for training.
- A `LinearRegression` model from `sklearn` was fitted to the historical release year and count data.
- Predictions for the next two years (2022 and 2023) were generated based on the trained model.
- The historical data and future predictions were visualized in a line plot.

## 7. Key Findings
Based on the analysis, the following insights were derived:
- **Movie Percentage**: Approximately 69.62% of the content on Netflix are movies.
- **TV Show Percentage**: Approximately 30.38% of the content on Netflix are TV shows.
- **Top Genre**: 'International Movies' is the most prevalent genre.
- **Top Country**: The 'United States' contributes the most content.
- **Latest Release Year**: The dataset includes content released up to 2021.
- **Future Predictions**: The model predicts around 383 titles for 2022 and 390 titles for 2023.

## 8. Conclusion
This analysis provides a comprehensive overview of the Netflix content library, revealing distribution patterns, popular genres and countries, and offering a basic forecast for future content growth. The insights gained can be valuable for content strategy and understanding platform evolution.
