import streamlit as st

# ---- PAGE CONFIG ----
st.set_page_config(page_title="AI Expo 1.0", layout="wide")

# ---- CUSTOM CSS ----
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #0E1117, #111827);
    color: white;
    font-family: 'Segoe UI', sans-serif;
}

/* Header */
.header {
    text-align: center;
    padding: 20px;
}
.header h1 {
    font-size: 40px;
    color: #00E5FF;
}
.header h2 {
    font-size: 22px;
    color: #A0AEC0;
}

/* Cards */
.card {
    background: #1F2937;
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 20px;
    transition: 0.3s;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.4);
}
.card:hover {
    transform: scale(1.02);
    box-shadow: 0px 8px 25px rgba(0,0,0,0.6);
}

/* Titles */
.title {
    font-size: 24px;
    color: #38BDF8;
    font-weight: bold;
}

/* Button */
a.button {
    display: inline-block;
    padding: 10px 15px;
    background: #00E5FF;
    color: black;
    border-radius: 8px;
    text-decoration: none;
    font-weight: bold;
}
a.button:hover {
    background: #38BDF8;
}

/* Section */
.section-title {
    font-size: 26px;
    margin-top: 20px;
    color: #FACC15;
}
</style>
""", unsafe_allow_html=True)

# ---- HEADER ----
st.markdown("""
<div class="header">
    <h1>🚀 AI Expo 1.0</h1>
    <h2>Shri G S Institute of Technology and Science, Indore</h2>
    <h2>Session - 2026</h2>
</div>
""", unsafe_allow_html=True)

# ---- TEAM & MENTORS ----
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="section-title">👩‍💻 Team Members</div>', unsafe_allow_html=True)
    st.write("""
    - Jitanjali Patel (0801IT231062)  
    - Arun Kushwah (0801IT231035)  
    - Dimple Chouhan (0801IT231046)
    """)

with col2:
    st.markdown('<div class="section-title">🎓 Mentors</div>', unsafe_allow_html=True)
    st.write("""
    - Dr. K K Sharma
    - Dr. Lalit Purohit  
    - Dr. Upendra Singh  
    - Mr. Akshay Gupta
    """)

st.write("---")

# ---- PROJECT CARD FUNCTION ----
def project_card(title, dataset, objective, model, performance, link):
    st.markdown(f"""
    <div class="card">
        <div class="title">{title}</div>
        <p><b>📂 Dataset:</b> {dataset}</p>
        <p><b>🎯 Objective:</b> {objective}</p>
        <p><b>⚙️ Model:</b> {model}</p>
        <p><b>📊 Performance:</b> {performance}</p>
        <a href="{link}" target="_blank" class="button">🚀 View Project</a>
    </div>
    """, unsafe_allow_html=True)

# ---- PROJECTS ----
st.markdown('<div class="section-title">💡 Projects Showcase</div>', unsafe_allow_html=True)

project_card(
    "✍️ Handwritten Digits & Operators Recognition",
    "Kaggle Image Dataset (200,331 samples, 16 classes, 28x28 images)",
    "Recognize handwritten digits and mathematical operators using deep learning.",
    "CNN (6 layers, BatchNorm, Dropout, Adam)",
    "Accuracy: 97.42% | F1-score: 97.42%",
    "https://handwrittendigitsandoperators-gvdahk3ls3srb5txjnkdzb.streamlit.app/"
)

project_card(
    "🎙️ Speech Sentiment Analysis",
    "Kaggle Audio Dataset (MFCC, Chroma, Mel Spectrogram features)",
    "Classify speech into Positive, Neutral, or Negative sentiment.",
    "ANN vs CNN vs LSTM (Best: CNN)",
    "Best Accuracy: 86%",
    "https://dimplechouhan-speech-sentiment.hf.space"
)

project_card(
    "🌪️ Disaster Risk Prediction",
    "Kaggle Tabular Dataset (20,000 records, 13 features)",
    "Predict whether a disaster is major or minor.",
    "Gaussian Naive Bayes + CatBoost",
    "Accuracy: 99.95% | AUC: 99.99%",
    "https://disaster-prediction-app-rhkugqyqhucplrtq8xkhrz.streamlit.app/"
)

project_card(
    "💳 Credit Card Fraud Detection",
    "European Card Dataset (Highly Imbalanced)",
    "Detect fraudulent transactions using imbalanced learning.",
    "SMOTE + XGBoost",
    "Accuracy: 99.9% | Recall: 89.8%",
    "https://fraud-detection-app-46rkw4vsx4y5scbndpe4ff.streamlit.app/"
)

project_card(
    "🏃 Human Activity Recognition",
    "UCF101 Video Dataset (15 classes, 1500 videos)",
    "Classify human activities from video clips.",
    "CNN + BiLSTM",
    "Accuracy: 87.33%",
    "https://huggingface.co/spaces/ArunKushwah/VisionAct_AI"
)

# ---- FOOTER ----
st.write("---")
st.markdown("""
<center>
✨ <b>AI Expo 1.0 | Innovative Machine Learning Solutions</b> ✨
</center>
""", unsafe_allow_html=True)
