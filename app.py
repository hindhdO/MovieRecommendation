import streamlit as st
import pickle
import pandas as pd
import modelcode


# Streamlit app
st.title("Movie Recommendation System")
st.write("Enter a movie you like, and we'll recommend similar movies!")

# Input for movie title
movie_title = st.selectbox("Select a movie:",modelcode. movies['title'].tolist())

# Slider for number of recommendations
top_n = st.slider("Number of recommendations", 1, 5, 3)

# Button to trigger recommendations
if st.button("Recommend"):
    recommendations = modelcode.recommend_movies(movie_title, top_n)
    st.write("Recommended Movies:")
    for movie in recommendations:
        st.write(movie)
