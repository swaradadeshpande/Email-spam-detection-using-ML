import streamlit as st
import pickle
import string
import nltk
import pandas as pd

from nltk.corpus import stopwords
from collections import Counter

import plotly.graph_objects as go
import plotly.express as px

# ---------------------------------
# NLTK
# ---------------------------------
nltk.download('stopwords')

# ---------------------------------
# PAGE CONFIG
# ---------------------------------
st.set_page_config(
    page_title="SpamShield AI",
    page_icon="🛡️",
    layout="wide"
)

# ---------------------------------
# CUSTOM CSS
# ---------------------------------
st.markdown("""
<style>

.stApp{
    background-color:#0b1120;
}

.hero{
    background:linear-gradient(
    -45deg,
    #00c6ff,
    #0072ff,
    #8e2de2,
    #4a00e0
    );

    background-size:400% 400%;

    animation:gradient 15s ease infinite;

    padding:40px;
    border-radius:20px;
    text-align:center;
    color:white;
    margin-bottom:20px;
}

@keyframes gradient{

0%{
background-position:0% 50%;
}

50%{
background-position:100% 50%;
}

100%{
background-position:0% 50%;
}
}

.card{

background:rgba(
255,
255,
255,
0.08
);

backdrop-filter:blur(12px);

padding:25px;

border-radius:20px;

border:1px solid rgba(
255,
255,
255,
0.15
);

margin-bottom:20px;
}

.footer{

text-align:center;
color:gray;
padding:20px;
margin-top:40px;
}

.result-spam{

background:#7f1d1d;

padding:20px;

border-radius:15px;

font-size:22px;

font-weight:bold;

color:white;
}

.result-ham{

background:#14532d;

padding:20px;

border-radius:15px;

font-size:22px;

font-weight:bold;

color:white;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------
# LOAD MODEL
# ---------------------------------
model = pickle.load(
    open("models/spam_model.pkl", "rb")
)

vectorizer = pickle.load(
    open("models/vectorizer.pkl", "rb")
)

# ---------------------------------
# SESSION STATE
# ---------------------------------
if "history" not in st.session_state:
    st.session_state.history = []

# ---------------------------------
# CLEANING FUNCTION
# ---------------------------------
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

# ---------------------------------
# SIDEBAR
# ---------------------------------
with st.sidebar:

    st.title("🛡️ SpamShield AI")

    st.markdown("---")

    st.success("Model: Random Forest")

    st.info("Accuracy: 97.29%")

    st.markdown("---")

    st.subheader("Features")

    st.write("✅ Spam Detection")
    st.write("✅ NLP Processing")
    st.write("✅ Risk Analysis")
    st.write("✅ Interactive Dashboard")
    st.write("✅ Data Visualizations")

    st.markdown("---")

    st.subheader("Dataset")

    st.write("Total Messages: 5572")
    st.write("Spam: 747")
    st.write("Ham: 4825")

# ---------------------------------
# HERO SECTION
# ---------------------------------
st.markdown("""
<div class="hero">

<h1>🛡️ SpamShield AI</h1>

<h3>Advanced Email & SMS Spam Detection System</h3>

<p>
Detect spam, phishing and suspicious messages using
Machine Learning, NLP and Interactive Analytics.
</p>

</div>
""", unsafe_allow_html=True)

# ---------------------------------
# STATS
# ---------------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Dataset Size", "5572")

with col2:
    st.metric("Accuracy", "97.29%")

with col3:
    st.metric("Model", "Random Forest")

# ---------------------------------
# INPUT CARD
# ---------------------------------
st.markdown('<div class="card">', unsafe_allow_html=True)

st.subheader("📧 Analyze Email or SMS")

message = st.text_area(
    "",
    height=220,
    placeholder="Paste your email or SMS message here..."
)

check = st.button(
    "🔍 Analyze Message",
    use_container_width=True
)

st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------------
# PREDICTION
# ---------------------------------
if check:

    if message.strip() == "":

        st.warning("Please enter a message.")

    else:

        cleaned = clean_text(message)

        vector = vectorizer.transform([cleaned])

        prediction = model.predict(vector)

        probability = model.predict_proba(vector)

        spam_prob = probability[0][1] * 100

        ham_prob = probability[0][0] * 100

        confidence = max(probability[0]) * 100

        word_count = len(message.split())

        char_count = len(message)

        # RESULT

        st.subheader("📊 Prediction Result")

        if prediction[0] == 1:

            st.markdown(
                f"""
                <div class="result-spam">
                🚨 SPAM MESSAGE DETECTED
                <br><br>
                Confidence: {confidence:.2f}%
                </div>
                """,
                unsafe_allow_html=True
            )

        else:

            st.markdown(
                f"""
                <div class="result-ham">
                ✅ LEGITIMATE MESSAGE
                <br><br>
                Confidence: {confidence:.2f}%
                </div>
                """,
                unsafe_allow_html=True
            )

        # SAVE HISTORY

        st.session_state.history.append({

            "Message": message[:60],

            "Prediction":
                "Spam"
                if prediction[0] == 1
                else "Ham",

            "Confidence":
                round(confidence, 2)
        })

        # ---------------------------------
        # ANALYTICS
        # ---------------------------------

        st.subheader("📈 Message Analytics")

        c1, c2, c3 = st.columns(3)

        with c1:
            st.metric("Words", word_count)

        with c2:
            st.metric("Characters", char_count)

        with c3:
            st.metric(
                "Spam Probability",
                f"{spam_prob:.2f}%"
            )

        # ---------------------------------
        # CHARTS
        # ---------------------------------

        col1, col2 = st.columns(2)

        with col1:

            gauge = go.Figure(
                go.Indicator(

                    mode="gauge+number",

                    value=spam_prob,

                    title={
                        'text':
                        "Spam Risk Score"
                    },

                    gauge={

                        'axis': {
                            'range': [0, 100]
                        },

                        'steps': [

                            {
                                'range': [0, 30],
                                'color': 'green'
                            },

                            {
                                'range': [30, 70],
                                'color': 'orange'
                            },

                            {
                                'range': [70, 100],
                                'color': 'red'
                            }
                        ]
                    }
                )
            )

            st.plotly_chart(
                gauge,
                use_container_width=True
            )

        with col2:

            donut = px.pie(

                names=[
                    "Ham",
                    "Spam"
                ],

                values=[
                    ham_prob,
                    spam_prob
                ],

                hole=0.65,

                title="Prediction Confidence"
            )

            st.plotly_chart(
                donut,
                use_container_width=True
            )

        # ---------------------------------
        # KEYWORD ANALYSIS
        # ---------------------------------

        st.subheader("🔑 Keyword Analysis")

        words = cleaned.split()

        top_words = Counter(words).most_common(10)

        if len(top_words) > 0:

            df_words = pd.DataFrame(

                top_words,

                columns=[
                    "Word",
                    "Frequency"
                ]
            )

            fig = px.bar(

                df_words,

                x="Word",

                y="Frequency",

                title="Most Frequent Keywords"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

# ---------------------------------
# MODEL COMPARISON
# ---------------------------------

st.subheader("🤖 Model Comparison")

model_df = pd.DataFrame({

    "Model": [

        "Naive Bayes",

        "Logistic Regression",

        "Random Forest"
    ],

    "Accuracy": [

        97.29,

        95.26,

        97.29
    ]
})

comparison = px.bar(

    model_df,

    x="Model",

    y="Accuracy",

    title="Machine Learning Model Performance",

    text="Accuracy"
)

st.plotly_chart(
    comparison,
    use_container_width=True
)

# ---------------------------------
# DATASET STATS
# ---------------------------------

st.subheader("📊 Dataset Statistics")

c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        "Total Messages",
        "5572"
    )

with c2:
    st.metric(
        "Spam Messages",
        "747"
    )

with c3:
    st.metric(
        "Ham Messages",
        "4825"
    )

# ---------------------------------
# HISTORY
# ---------------------------------

st.subheader("📝 Prediction History")

if len(st.session_state.history) > 0:

    history_df = pd.DataFrame(
        st.session_state.history
    )

    st.dataframe(
        history_df,
        use_container_width=True
    )

else:

    st.info(
        "No predictions made yet."
    )

# ---------------------------------
# SAMPLE MESSAGES
# ---------------------------------

st.subheader("📌 Example Messages")

col1, col2 = st.columns(2)

with col1:

    st.error("""
Congratulations!

You have won a FREE iPhone.

Click the link below to claim your reward.
""")

with col2:

    st.success("""
Hello Swarada,

Your project review meeting is scheduled
for tomorrow at 10:00 AM.

Regards,
Team
""")

# ---------------------------------
# FOOTER
# ---------------------------------

st.markdown("""
<div class="footer">

Built with ❤️ using
Python • NLP • Random Forest • Plotly • Streamlit

</div>
""", unsafe_allow_html=True)