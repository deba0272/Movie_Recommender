import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

# Load data
movie_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# CSS
st.markdown(
    """
    <style>
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }

    .main {
        background-color: #f5f5f5;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        animation: fadeIn 2s;
    }
    .title {
        font-size: 48px;
        color: #2c3e50;
        animation: fadeIn 2s;
        margin-bottom: 0;
    }
    .subtitle {
        font-size: 24px;
        color: #34495e;
        animation: fadeIn 2s;
    }
    .movie-title {
        font-size: 20px;
        font-weight: bold;
        color: #8e44ad;
        animation: fadeIn 2s;
    }
    .numbered-list {
        list-style-type: decimal;
        text-align: left;
        padding-left: 40%;
        animation: fadeIn 2s;
    }
    .numbered-list li {
        margin: 10px 0;
        animation: fadeIn 2s;
    }
    .footer {
        background-color: #2c3e50;
        color: #ffffff;
        padding: 20px;
        position: fixed;
        bottom: 0;
        width: 700px;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown('<div class="main">', unsafe_allow_html=True)
st.markdown('<div class="title">Movie Recommender System</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Get recommendations based on your favorite movies</div>', unsafe_allow_html=True)

selected_movie_name = st.selectbox(
    'Select a movie:',
    movies['title'].values
)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    st.markdown('<div class="subtitle">Recommended Movies:</div>', unsafe_allow_html=True)
    st.markdown('<ol class="numbered-list">', unsafe_allow_html=True)
    for movie in recommendations:
        st.markdown(f'<li class="movie-title">{movie}</li>', unsafe_allow_html=True)
    st.markdown('</ol>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown(
    """
    <div class="footer">
        Developed by Debajyoti | <a href="https://github.com/deba0272" style="color: #ffffff;">GitHub</a> | <a href="https://www.linkedin.com/in/debajyoti-roy-a1a7bb230/" style="color: #ffffff;">LinkedIn</a>
    </div>
    """,
    unsafe_allow_html=True
)
