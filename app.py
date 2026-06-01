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

/* Main App Background */
.stApp{
    background: linear-gradient(
        135deg,
        #f4f7ff 0%,
        #eef2ff 100%
    );
}

/* Main Text */
html, body, [class*="css"]{
    color:#1f2937;
}

/* Hero Section */
.hero{
    background: linear-gradient(
        135deg,
        #4f46e5,
        #7c3aed,
        #2563eb
    );

    padding:45px;

    border-radius:25px;

    text-align:center;

    color:white;

    margin-bottom:25px;

    box-shadow:0px 10px 30px rgba(
        79,
        70,
        229,
        0.3
    );
}

/* Glass Card */
.card{

    background:white;

    padding:25px;

    border-radius:20px;

    box-shadow:
    0px 4px 25px rgba(
        0,
        0,
        0,
        0.08
    );

    margin-bottom:25px;
}

/* Metric Cards */
[data-testid="metric-container"]{

    background:white;

    border-radius:16px;

    padding:15px;

    box-shadow:
    0px 4px 15px rgba(
        0,
        0,
        0,
        0.08
    );

    border:1px solid #e5e7eb;
}

/* Text Area */
textarea{

    border-radius:15px !important;

    border:2px solid #dbeafe !important;

    background:#ffffff !important;

    color:#111827 !important;

    font-size:16px !important;
}

/* Analyze Button */
.stButton > button{

    width:100%;

    height:55px;

    border:none;

    border-radius:15px;

    background:linear-gradient(
        135deg,
        #4f46e5,
        #7c3aed
    );

    color:white;

    font-size:18px;

    font-weight:600;

    transition:0.3s;
}

.stButton > button:hover{

    transform:translateY(-2px);

    box-shadow:
    0px 8px 20px rgba(
        79,
        70,
        229,
        0.4
    );
}

/* Spam Result */
.result-spam{

    background:linear-gradient(
        135deg,
        #ef4444,
        #dc2626
    );

    color:white;

    padding:25px;

    border-radius:20px;

    font-size:22px;

    font-weight:bold;

    box-shadow:
    0px 8px 20px rgba(
        239,
        68,
        68,
        0.3
    );
}

/* Ham Result */
.result-ham{

    background:linear-gradient(
        135deg,
        #10b981,
        #059669
    );

    color:white;

    padding:25px;

    border-radius:20px;

    font-size:22px;

    font-weight:bold;

    box-shadow:
    0px 8px 20px rgba(
        16,
        185,
        129,
        0.3
    );
}

/* Sidebar */
section[data-testid="stSidebar"]{

    background:linear-gradient(
        180deg,
        #1e1b4b,
        #312e81
    );
}

section[data-testid="stSidebar"] *{

    color:white !important;
}

/* DataFrame */
[data-testid="stDataFrame"]{

    background:white;

    border-radius:15px;
}

/* Footer */
.footer{

    text-align:center;

    color:#6b7280;

    font-size:14px;

    margin-top:40px;

    padding:20px;
}

/* Headers */
h1,h2,h3{

    color:#111827;
}

.hero h1,
.hero h2,
.hero h3,
.hero p{

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

Built using
Python • NLP • Random Forest • Plotly • Streamlit

</div>
""", unsafe_allow_html=True)