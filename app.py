import streamlit as st
import pickle
import joblib

st.title("Movie Recommendation System")

with open("movie.pkl", "rb") as f:
    movies = pickle.load(f)

similarity = joblib.load("similarity.pkl")

movie_list = movies['title'].values

# Recommendation function
def recommend(selected_movie):
    movie_index = movies[movies['title'] == selected_movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommendations = []

    for i in movies_list:
        recommendations.append(movies.iloc[i[0]].title)
    return recommendations

selected_movie = st.selectbox("Select a movie:", movie_list)

if st.button("Recommend"):
    recommendations = recommend(selected_movie)
    st.write(f"Recommendations after {selected_movie} you should watch:")

    for i in recommendations:
        st.write(i)