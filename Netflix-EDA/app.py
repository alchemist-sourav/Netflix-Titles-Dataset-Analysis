import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("🎬 Netflix Titles Dashboard")

uploaded_file = st.file_uploader(
    "Upload Netflix Dataset",
    type=["csv"]
)

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    df['date_added'] = pd.to_datetime(
        df['date_added'],
        errors='coerce'
    )

    st.subheader("Dataset Overview")

    st.write(df.head())

    # Movie vs TV Show
    st.subheader("Movies vs TV Shows")

    fig, ax = plt.subplots()

    df['type'].value_counts().plot(
        kind='pie',
        autopct='%1.1f%%',
        ax=ax
    )

    ax.set_ylabel("")

    st.pyplot(fig)

    # Release Trend
    st.subheader("Release Trend")

    yearly = (
        df.groupby('release_year')
        .size()
        .reset_index(name='count')
    )

    fig, ax = plt.subplots()

    sns.lineplot(
        data=yearly,
        x='release_year',
        y='count',
        ax=ax
    )

    st.pyplot(fig)

    # Top Genres
    st.subheader("Top Genres")

    genres = (
        df['listed_in']
        .str.split(',')
        .explode()
        .str.strip()
    )

    top_genres = genres.value_counts().head(10)

    fig, ax = plt.subplots()

    sns.barplot(
        x=top_genres.values,
        y=top_genres.index,
        ax=ax
    )

    st.pyplot(fig)