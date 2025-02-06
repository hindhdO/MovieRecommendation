import streamlit as st
import pickle
import pandas as pd
import modelcode
import requests 

TMDB_API_KEY = "6971a6abf45de5c07f9a7f9a180a83db"
TMDB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"


def fetch_poster(movie_title):
    try:
        
        search_url = f"https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&query={movie_title}"
        response = requests.get(search_url)
        response.raise_for_status()
        data = response.json()
        if data["results"]:
            poster_path = data["results"][0]["poster_path"]
            return f"{TMDB_IMAGE_URL}{poster_path}"
    except Exception as e:
        st.error(f"Error fetching poster for {movie_title}: {e}")
    return None

# Streamlit app
st.title("Movie Recommendation System")
st.write("Enter a movie you like, and we'll recommend similar movies!")

movie_title = st.selectbox("Select a movie:", modelcode.movies['title'].tolist())
top_n = st.slider("Number of recommendations", 1, 5, 3)
if st.button("Recommend"):
    recommendations = modelcode.recommend_movies(movie_title, top_n)
    st.write("Recommended Movies:")
    
    columns = st.columns(len(recommendations)) 
    
    for idx, movie in enumerate(recommendations):
        with columns[idx]: 
            st.write(movie) 
            poster_url = fetch_poster(movie)  
            if poster_url:
                st.image(poster_url, caption=movie, width=150)  
            else:
                st.write("Poster not available")
