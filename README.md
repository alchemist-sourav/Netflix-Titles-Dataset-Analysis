# 🎬 Netflix Titles Dashboard

A Streamlit web application for Exploratory Data Analysis (EDA) of Netflix titles. This dashboard allows users to upload a Netflix dataset (CSV format) and generates interactive visualizations to uncover insights about the content available on the platform.

## Features

- **Data Overview**: View the raw data in a tabular format.
- **Movies vs. TV Shows**: A pie chart comparing the proportion of movies and TV shows on Netflix.
- **Release Trend**: A line graph showing the trend of content releases over the years.
- **Top Genres**: A bar chart displaying the top 10 most popular genres on the platform.

## Prerequisites

Make sure you have Python installed. You will need the following Python libraries:
- `streamlit`
- `pandas`
- `matplotlib`
- `seaborn`

You can install them using pip:

```bash
pip install streamlit pandas matplotlib seaborn
```

## Running the App

1. Clone or download this repository to your local machine.
2. Open a terminal or command prompt and navigate to the project directory.
3. Run the following command to start the Streamlit app:

```bash
streamlit run app.py
```

4. The app will open in your default web browser (usually at `http://localhost:8501`).

## Usage

1. Open the app in your browser.
2. Click on the "Browse files" button to upload your Netflix dataset (`netflix_titles.csv`).
3. The dashboard will automatically populate with visualizations based on the uploaded data.

## Dataset

You can use the standard Netflix Movies and TV Shows dataset available on platforms like Kaggle. The dataset should contain columns such as `type`, `release_year`, `date_added`, and `listed_in`.
