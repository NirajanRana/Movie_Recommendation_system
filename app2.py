import pickle
import streamlit as st
import pandas as pd
import requests
from textblob import TextBlob  # For Sentiment Analysis

# --- Load data ---
movie_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))
all_reviews_df = pickle.load(open('movie_reviews_dataset.pkl', 'rb'))

# --- Function to fetch poster from TMDB ---
def fetch_poster(movie_id):
    api_key = "862bae8cf828e3fa4ea288a97db04982"
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US&api_key={api_key}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            poster_path = data.get('poster_path')
            return f"https://image.tmdb.org/t/p/w500/{poster_path}" if poster_path else ""
        else:
            return ""
    except Exception as e:
        st.error(f"Error fetching poster: {e}")
        return ""

# --- Fetch reviews locally ---
def fetch_reviews_local(movie_id):
    reviews_row = all_reviews_df[all_reviews_df['movie_id'] == int(movie_id)]
    if not reviews_row.empty:
        return reviews_row.iloc[0]['reviews']
    else:
        return []

# --- Sentiment Analysis Function ---
def analyze_sentiment(review_text):
    analysis = TextBlob(review_text)
    polarity = analysis.sentiment.polarity
    if polarity < -0.2:
        return "negative"
    else:
        return "positive_or_neutral"

# --- Recommend movies ---
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

    recommended_movie_names = []
    recommended_movie_posters = []
    recommended_movie_ids = []

    for i in distances[1:6]:
        movie_id = str(movies.iloc[i[0]]['movie_id'])
        recommended_movie_ids.append(movie_id)
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names, recommended_movie_posters, recommended_movie_ids

# --- Streamlit UI ---
st.title('🎬 Movie Recommender System with Color-Coded Reviews')

movie_list = movies['title'].values
selected_movie = st.selectbox("Type or select a movie from the dropdown", movie_list)

if st.button('Show Recommendations'):
    with st.spinner('Fetching recommendations...'):
        recommended_movie_names, recommended_movie_posters, recommended_movie_ids = recommend(selected_movie)

    st.markdown("---")
    cols = st.columns(5)
    for idx, col in enumerate(cols):
        with col:
            st.image(recommended_movie_posters[idx], use_container_width=True)
            st.caption(recommended_movie_names[idx])

            reviews = fetch_reviews_local(recommended_movie_ids[idx])
            if isinstance(reviews, list) and reviews:
                st.markdown("**Top Reviews:**")
                for review_text in reviews[:2]:  # Show top 2 reviews
                    sentiment = analyze_sentiment(review_text)
                    if sentiment == "negative":
                        color = "red"
                    else:
                        color = "green"  # positive OR neutral both green

                    st.markdown(
                        f"<p style='color:{color};font-size:14px;'>\"{review_text}\"</p>",
                        unsafe_allow_html=True
                    )
            else:
                st.write("No reviews found.")
