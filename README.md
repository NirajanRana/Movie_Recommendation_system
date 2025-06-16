https://movierecommendatiosystem-9pxzrl4d29l5getxtguwey.streamlit.app/
# 🎬 Movie Recommendation System & Reviews Analysis

This repository contains two Jupyter Notebooks focused on movie review analysis and recommendation system development using machine learning and natural language processing techniques.

---

## 📁 Contents

### 1. `movie_recommendation_system.ipynb`

#### 📌 Description
This notebook implements a **content-based movie recommendation system**. It uses movie metadata (such as genre, director, cast, etc.) to suggest similar movies to a given input.

#### 🧠 Key Features
- Data preprocessing using pandas and scikit-learn
- Feature extraction using TF-IDF and count vectorization
- Cosine similarity computation for recommendation
- Retrieval of top N similar movies

#### 🔧 Technologies Used
- Python  
- pandas, numpy  
- scikit-learn (TF-IDF, CountVectorizer, cosine_similarity)

#### 📝 Example
Given a movie like _"The Dark Knight"_, the system returns a list of most similar movies based on textual metadata.

---

### 2. `reviews.ipynb`

#### 📌 Description
This notebook performs **sentiment analysis on movie reviews**, classifying reviews as positive or negative using text classification techniques.

#### 🧠 Key Features
- Text preprocessing: tokenization, stopword removal, stemming
- Feature engineering using Bag-of-Words or TF-IDF
- Model training (e.g., Naive Bayes, Logistic Regression)
- Model evaluation with accuracy and confusion matrix

#### 🔧 Technologies Used
- Python  
- pandas, nltk  
- scikit-learn (text vectorization, model training and evaluation)

#### 📝 Example
Given a sample review like _"The movie was excellent!"_, the model predicts it as a **positive** sentiment.

---

## 🛠 Installation & Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/movie-recommendation-and-review-analysis.git
   cd movie-recommendation-and-review-analysis
