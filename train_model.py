import pandas as pd
import pickle
import string
import nltk

from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score, classification_report
from sklearn.ensemble import RandomForestClassifier

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

# Convert labels
df['label'] = df['label'].map({
    'ham': 0,
    'spam': 1
})

# Feature Extraction
vectorizer = TfidfVectorizer(max_features=3000)

X = vectorizer.fit_transform(df['message'])

y = df['label']

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train Model
rf_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

rf_model.fit(X_train, y_train)

rf_pred = rf_model.predict(X_test)

print("Random Forest Accuracy:",
      accuracy_score(y_test, rf_pred))
print("\nClassification Report:\n")
print(classification_report(y_test, rf_pred))

# Save Model
pickle.dump(
    rf_model,
    open("models/spam_model.pkl", "wb")
)

pickle.dump(
    vectorizer,
    open("models/vectorizer.pkl", "wb")
)

print("\nModel Saved Successfully!")