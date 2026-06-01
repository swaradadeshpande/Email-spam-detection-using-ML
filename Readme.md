# 📧 Email Spam Detection using Machine Learning

## 🚀 Project Overview

Email spam has become one of the most common cybersecurity and communication challenges. Spam emails often contain advertisements, scams, phishing links, malicious attachments, or fraudulent content that can compromise user security.

This project aims to build an intelligent Email Spam Detection System using Machine Learning and Natural Language Processing (NLP) techniques. The system automatically classifies incoming messages as **Spam** or **Ham (Legitimate Email)**, helping users identify unwanted and potentially dangerous emails.

---

## 🎯 Problem Statement

Spam emails are sent in bulk and frequently contain misleading or malicious content. Manually filtering these emails is inefficient and error-prone.

The objective of this project is to:

* Analyze email text data.
* Preprocess and clean textual content.
* Extract meaningful features using NLP techniques.
* Train Machine Learning models for classification.
* Predict whether a new email is Spam or Ham.
* Evaluate model performance using industry-standard metrics.

---

## 📊 Dataset Information

The project uses the SMS Spam Collection Dataset containing labeled messages.

### Features

| Column | Description               |
| ------ | ------------------------- |
| v1     | Target Label (Spam/Ham)   |
| v2     | Email/SMS Message Content |

### Dataset Statistics

* Total Records: 5572
* Classes:

  * Spam
  * Ham (Legitimate)

---

## 🛠️ Technologies Used

### Programming Language

* Python 3.x

### Libraries

* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* NLTK
* WordCloud
* Pickle
* Streamlit

---

## 📂 Project Structure

```text
Email-Spam-Detection-ML/
│
├── dataset/
│   └── spam.csv
│
├── notebooks/
│   └── analysis.ipynb
│
├── models/
│   ├── spam_model.pkl
│   └── vectorizer.pkl
│
├── app.py
├── spam_detector.py
├── requirements.txt
├── README.md
└── screenshots/
```

---

## 🔄 Project Workflow

### 1. Data Collection

* Load dataset using Pandas.
* Inspect dataset structure.

### 2. Data Cleaning

* Remove unnecessary columns.
* Handle duplicates.
* Check missing values.
* Rename columns.

### 3. Exploratory Data Analysis (EDA)

* Spam vs Ham distribution.
* Message length analysis.
* Frequency analysis.
* Word Cloud visualization.

### 4. Text Preprocessing

The text is cleaned using:

* Lowercasing
* Punctuation Removal
* Stopword Removal
* Tokenization

### 5. Feature Engineering

TF-IDF Vectorization converts textual data into numerical features.

### 6. Model Training

Machine Learning models used:

* Multinomial Naive Bayes
* Logistic Regression
* Random Forest Classifier

### 7. Model Evaluation

Performance metrics:

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix

### 8. Prediction System

Users can enter custom messages and receive predictions:

```text
Input:
"Congratulations! You have won a free iPhone."

Output:
Spam
```

---

## 📈 Exploratory Data Analysis

### Spam vs Ham Distribution

* Visualized class imbalance.
* Identified dataset composition.

### Message Length Analysis

* Compared average message lengths.
* Analyzed distribution patterns.

### Word Cloud Analysis

Generated separate word clouds for:

* Spam Messages
* Ham Messages

---

## 🤖 Machine Learning Models

### Multinomial Naive Bayes

Most suitable for text classification tasks.

### Logistic Regression

Provides strong baseline performance.

### Random Forest

Used for comparison and benchmarking.

---

## 📊 Evaluation Metrics

The model is evaluated using:

```text
Accuracy Score
Precision
Recall
F1-Score
Confusion Matrix
Classification Report
```

Expected Accuracy:

```text
97% - 99%
```

---

## 💻 Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/email-spam-detection-ml.git
```

### Move to Project Directory

```bash
cd email-spam-detection-ml
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

### Run Training Script

```bash
python spam_detector.py
```

### Run Streamlit Application

```bash
streamlit run app.py
```

---

## 📷 Sample Results

### Example 1

```text
Input:
Congratulations! Claim your free reward now.

Prediction:
Spam
```

### Example 2

```text
Input:
Hi, are we meeting tomorrow at 10 AM?

Prediction:
Ham
```

---

## 🔍 Future Enhancements

* Deep Learning-based Spam Detection
* LSTM and GRU Models
* Transformer Models (BERT)
* Email Attachment Analysis
* URL Safety Detection
* Real-Time Email Filtering
* Web Deployment using Flask/Django
* Cloud Deployment using AWS

---

## 🎓 Learning Outcomes

Through this project, the following concepts were implemented:

* Data Cleaning
* Exploratory Data Analysis
* Natural Language Processing
* Feature Engineering
* TF-IDF Vectorization
* Supervised Machine Learning
* Model Evaluation
* Model Deployment

---

## 🌟 Key Highlights

✅ End-to-End Machine Learning Project

✅ Natural Language Processing Implementation

✅ Multiple Model Comparison

✅ Interactive Prediction System

✅ Resume-Friendly Data Science Project

✅ Real-World Cybersecurity Application

---

## 📚 References

* Scikit-Learn Documentation
* NLTK Documentation
* Pandas Documentation
* NumPy Documentation
* Streamlit Documentation
* UCI Machine Learning Repository

---

## 👨‍💻 Author

**Swarada**

Data Science | Machine Learning | Python Developer

If you found this project useful, don't forget to ⭐ the repository.
