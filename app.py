import streamlit as st
import pickle
import pandas as pd

# Open the file for reading in binary mode using a with statement
with open('movies_dict.pkl', 'rb') as f:
    movies_dict = pickle.load(f)
with open('similarity.pkl', 'rb') as f:
    similarity = pickle.load(f)
movies=pd.DataFrame(movies_dict)

def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movies=[]
    for i in movies_list:
        movie_id=i[0]
        
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

st.title('Movie Recommender System')
selected_movie_name=st.selectbox("select the movie:",movies['title'].values)
if st.button('Recommend'):
    recomendations=recommend(selected_movie_name)
    for i in recomendations:
        st.write(i)