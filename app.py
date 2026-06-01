import streamlit as st
import pickle
import string
import nltk

from nltk.corpus import stopwords

nltk.download('stopwords')

# Load model
model = pickle.load(
    open("models/spam_model.pkl", "rb")
)

vectorizer = pickle.load(
    open("models/vectorizer.pkl", "rb")
)

# Cleaning Function
def clean_text(text):

    text = text.lower()

    text = ''.join(
        char for char in text
        if char not in string.punctuation
    )

    words = text.split()

    words = [
        word for word in words
        if word not in stopwords.words('english')
    ]

    return " ".join(words)

# UI
st.set_page_config(
    page_title="Spam Detector",
    page_icon="📧"
)

st.title("📧 Email Spam Detection System")

st.write(
    "Detect whether a message is Spam or Ham using Machine Learning."
)

message = st.text_area(
    "Enter Email / SMS Message"
)

if st.button("Check Message"):

    cleaned = clean_text(message)

    vector = vectorizer.transform([cleaned])

    prediction = model.predict(vector)

    if prediction[0] == 1:
        st.error("🚨 Spam Message")
    else:
        st.success("✅ Legitimate Message")