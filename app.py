import streamlit as st
import pickle
import pandas as pd
import requests

def fetchposter(movieid):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=3acf61d7347143c7bc3fc31b7e32f839'.format(movieid))
    data1 = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data1['poster_path']

def recommend(movie):
    movieindex = movies[movies['title'] == movie].index[0]
    distances = similarity[movieindex]
    movieslist = sorted(list(enumerate(distances)), reverse = True,key = lambda x:x[1])[1:6]

    recommendmovies = []
    recommendmoviesposters = []
    for i in movieslist:
        movieid = movies.iloc[i[0]].movie_id

        recommendmovies.append(movies.iloc[i[0]].title)
        #fetch poster from api
        recommendmoviesposters.append(fetchposter(movieid))
    return recommendmovies,recommendmoviesposters

movies = pickle.load(open('movies.pkl','rb'))
similarity = pickle.load(open('similar.pkl','rb'))

st.title('Suggest Movies')
selectedmoviename = st.selectbox('Please Choose Movie', movies['title'].values)

if st.button('suggest'):
    names,posters = recommend(selectedmoviename)



    col1,col2,col3, col4,col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])