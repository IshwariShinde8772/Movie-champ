import streamlit as st
import pickle
import pandas as pd
import requests
from dotenv import load_dotenv
load_dotenv()
import os
TMDB_BEARER_TOKEN = os.getenv("TMDB_BEARER_TOKEN")



# ================== TMDB CONFIG ==================
TMDB_MOVIE_DETAILS_URL = "https://api.themoviedb.org/3/movie/{}"
TMDB_IMAGE_BASE_URL = "https://image.tmdb.org/t/p/w500"

headers = {
    "Authorization": f"Bearer {TMDB_BEARER_TOKEN}",
    "accept": "application/json"
}

# ================== LOAD DATA ==================
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

# ================== FUNCTIONS ==================
def fetch_poster(movie_id):
    try:
        url = TMDB_MOVIE_DETAILS_URL.format(movie_id)
        response = requests.get(url, headers=headers)
        data = response.json()

        poster_path = data.get('poster_path')
        if poster_path:
            return TMDB_IMAGE_BASE_URL + poster_path
        else:
            return "https://via.placeholder.com/500x750?text=No+Image"
    except:
        return "https://via.placeholder.com/500x750?text=Error"

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []
    recommended_posters = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_posters

# ================== STREAMLIT UI ==================
st.set_page_config(page_title="Movie Recommender", layout="wide")

st.title("🎬 Movie Recommender System")
st.write("Select a movie and get top 5 similar recommendations")

selected_movie_name = st.selectbox(
    "Choose a movie:",
    movies['title'].values
)

if st.button("Recommend"):
    names, posters = recommend(selected_movie_name)

    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.image(posters[i])
            st.caption(names[i])
