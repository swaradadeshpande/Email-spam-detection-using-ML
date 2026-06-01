import streamlit as st
import pickle
import string
import nltk

from nltk.corpus import stopwords

nltk.download('stopwords')

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="SpamShield AI",
    page_icon="🛡️",
    layout="wide"
)

# -----------------------------
# CUSTOM CSS
# -----------------------------
st.markdown("""
<style>

.main {
    background-color: #0f172a;
}

.hero {
    padding: 25px;
    border-radius: 15px;
    text-align: center;
    background: linear-gradient(
        135deg,
        #2563eb,
        #7c3aed
    );
    color: white;
}

.card {
    background-color: #1e293b;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0px 0px 15px rgba(0,0,0,0.3);
}

.result-spam {
    background-color: #7f1d1d;
    padding: 15px;
    border-radius: 10px;
    color: white;
    font-size: 20px;
    font-weight: bold;
}

.result-ham {
    background-color: #14532d;
    padding: 15px;
    border-radius: 10px;
    color: white;
    font-size: 20px;
    font-weight: bold;
}

.footer {
    text-align:center;
    color:gray;
    margin-top:40px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# LOAD MODEL
# -----------------------------
model = pickle.load(
    open("models/spam_model.pkl", "rb")
)

vectorizer = pickle.load(
    open("models/vectorizer.pkl", "rb")
)

# -----------------------------
# CLEAN TEXT
# -----------------------------
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

# -----------------------------
# SIDEBAR
# -----------------------------
with st.sidebar:

    st.title("🛡️ SpamShield AI")

    st.markdown("---")

    st.markdown("""
### About

This application uses:

- TF-IDF Vectorization
- Machine Learning
- NLP Text Processing
- Spam Classification

### Model

Random Forest Classifier

### Accuracy

97.29%
""")

# -----------------------------
# HERO SECTION
# -----------------------------
st.markdown("""
<div class="hero">
<h1>📧 SpamShield AI</h1>
<h3>Email & SMS Spam Detection System</h3>
<p>Detect malicious, phishing and spam messages instantly using Machine Learning.</p>
</div>
""", unsafe_allow_html=True)

st.write("")

# -----------------------------
# STATS
# -----------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Dataset Size", "5572")

with col2:
    st.metric("Accuracy", "97.29%")

with col3:
    st.metric("Model", "Random Forest Classifie")

st.write("")

# -----------------------------
# INPUT SECTION
# -----------------------------
st.markdown('<div class="card">', unsafe_allow_html=True)

st.subheader("✉️ Enter Message")

message = st.text_area(
    "",
    height=200,
    placeholder="Type or paste your email/SMS message here..."
)

check = st.button("🔍 Analyze Message")

st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------
# PREDICTION
# -----------------------------
if check:

    if len(message.strip()) == 0:
        st.warning("Please enter a message.")

    else:

        cleaned = clean_text(message)

        vector = vectorizer.transform([cleaned])

        prediction = model.predict(vector)

        probability = model.predict_proba(vector)

        confidence = max(probability[0]) * 100

        st.write("")

        st.subheader("📊 Analysis Result")

        if prediction[0] == 1:

            st.markdown(f"""
            <div class="result-spam">
            🚨 SPAM MESSAGE DETECTED
            <br><br>
            Confidence: {confidence:.2f}%
            </div>
            """, unsafe_allow_html=True)

        else:

            st.markdown(f"""
            <div class="result-ham">
            ✅ LEGITIMATE MESSAGE
            <br><br>
            Confidence: {confidence:.2f}%
            </div>
            """, unsafe_allow_html=True)

# -----------------------------
# SAMPLE MESSAGES
# -----------------------------
st.write("")
st.subheader("📌 Sample Messages")

col1, col2 = st.columns(2)

with col1:
    st.info("""
Congratulations!

You have won a FREE iPhone.

Click here to claim now.
""")

with col2:
    st.success("""
Hi Swarada,

Our meeting is scheduled tomorrow at 10 AM.

Regards,
Team
""")

# -----------------------------
# FOOTER
# -----------------------------
st.markdown("""
<div class="footer">
Built with ❤️ using Python, NLP, Scikit-Learn and Streamlit
</div>
""", unsafe_allow_html=True)

