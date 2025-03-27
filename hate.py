import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

# Load pre-trained model and vectorizer
model = joblib.load('hate_speech_model.pkl')
vectorizer = joblib.load('tfidf_vectorizer.pkl')

# Streamlit app
st.title("Hate Speech Detection App")
st.write("Enter a paragraph to check for hate speech:")

# Text input
user_input = st.text_area("Input Text", "")

if st.button("Check for Hate Speech"):
    if user_input:
        # Vectorize the input text
        text_vectorized = vectorizer.transform([user_input])
        
        # Predict using the model
        prediction = model.predict(text_vectorized)
        
        # Display result
        if prediction[0] == 1:
            st.error("This text contains hate speech.")
        else:
            st.success("This text does not contain hate speech.")
    else:
        st.warning("Please enter some text to analyze.")