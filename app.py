import streamlit as st
import pickle
import pandas as pd
  
def recommend(movie):
  movie_index=movies[movies['Series_Title'] == movie].index[0]
  distance=similarity[movie_index]
  movie_recommended=sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]
  recommendMovies=[]
  recommendMoviesPosters=[]
  for i in movie_recommended:
    recommendMovies.append(movies.iloc[i[0]].Series_Title)
    recommendMoviesPosters.append(movies.iloc[i[0]].Poster_Link)
  return recommendMovies,recommendMoviesPosters      
movies= pickle.load(open('movies.pkl','rb'))
similarity= pickle.load(open('similarity.pkl','rb'))
movies=pd.DataFrame(movies)
st.title('Movie Recommender System')
selected_movie=st.selectbox("Select the movie from the given list of movies",movies['Series_Title'].values)
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)
if st.button('Recommend'):
  name,posters=recommend(selected_movie)
  st.write('Here are Top 5 Movie Recommendations for you!')
  col1,col2,col3,col4,col5=st.columns(5,gap="small")
 
  with st.container():
    with col1:
        st.text(name[0])
        st.image(posters[0])
    with col2:
        st.text(name[1])
        st.image(posters[1])
    with col3:
        st.text(name[2])
        st.image(posters[2])
    with col4:
        st.text(name[3])
        st.image(posters[3])
    with col5:
        st.text(name[4])
        st.image(posters[4])
           

