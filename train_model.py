import pandas as pd
import pickle
import string
import nltk

from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# Download stopwords
nltk.download('stopwords')

# Load Dataset
df = pd.read_csv("dataset/spam.csv", encoding="latin-1")

# Keep only useful columns
df = df[['v1', 'v2']]

# Rename columns
df.columns = ['label', 'message']

# Remove duplicates
df.drop_duplicates(inplace=True)

# Text Cleaning Function
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

# Apply cleaning
df['message'] = df['message'].apply(clean_text)