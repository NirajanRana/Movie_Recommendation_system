import pickle

import pandas as pd
import streamlit as st



def recommend(movie):
    movie_index = movies[movies['title'] ==movie].index[0]
    distances = similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies


st.header('Movie Recommender System')
similarity = pickle.load(open('similarity.pkl','rb'))

movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)

selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movies['title'].values
)

if st.button('recommend'):
    recommendations=recommend(selected_movie)
    for i in recommendations:
        st.write(i)

