import streamlit as st
import pandas as pd

# ---------------- Load Dataset ----------------
@st.cache_data
def load_data():
    movies = pd.read_csv("movies.csv")
    ratings = pd.read_csv("ratings.csv")
    return movies, ratings

movies, ratings = load_data()

# ---------------- Extract All Genres ----------------
all_genres = set()

for g in movies['genres']:
    for genre in g.split('|'):
        all_genres.add(genre)

all_genres = sorted(list(all_genres))


# ---------------- Recommendation Function ----------------
def recommend_movies_by_genre(selected_genres, top_n=10):

    # Filter movies by selected genres
    filtered_movies = movies[movies['genres'].apply(
        lambda x: any(g in x for g in selected_genres)
    )]

    # Merge ratings
    movie_ratings = ratings.merge(filtered_movies, on="movieId")

    # Average rating of each movie
    avg_ratings = movie_ratings.groupby("title")["rating"].mean()

    # Sort by rating
    top_movies = avg_ratings.sort_values(ascending=False).head(top_n)

    return top_movies.index.tolist()


# ---------------- Streamlit UI ----------------
st.title("🎬 Smart Movie Recommendation System")

st.write("First choose what kind of movies you like.")

selected_genres = st.multiselect(
    "Select Movie Genres",
    all_genres
)

if st.button("Recommend Movies"):

    if len(selected_genres) == 0:
        st.warning("Please select at least one genre")

    else:
        recommendations = recommend_movies_by_genre(selected_genres)

        st.subheader("🎥 Recommended Movies")

        for i, movie in enumerate(recommendations, 1):
            st.write(f"{i}. {movie}")