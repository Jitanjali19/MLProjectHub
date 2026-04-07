import streamlit as st

st.markdown("""
<style>
.stApp {
    background-color: #0E1117;
    color: white;
}
</style>
""", unsafe_allow_html=True)

st.set_page_config(page_title="ML Projects Hub", layout="wide")

# ---- HEADER ----
st.title("🚀 Machine Learning Projects Portfolio")
st.markdown("### 👩‍💻 Team: Jitanjali Patel | Arun Kushwah | Dimple Chouhan")
st.markdown("🏫 Shri G.S. Institute of Technology & Science, Indore")

st.write("---")

# ---- FUNCTION FOR CARD ----
def project_card(title, dataset, objective, model, performance, link):
    st.markdown(f"## 🔷 {title}")
    st.write(f"**📂 Dataset:** {dataset}")
    st.write(f"**🎯 Objective:** {objective}")
    st.write(f"**⚙️ Model:** {model}")
    st.write(f"**📊 Performance:** {performance}")
    st.markdown(f"[🚀 Open Project]({link})", unsafe_allow_html=True)
    st.write("---")


# ---- PROJECTS ----

project_card(
    "Handwritten Digits & Operators Recognition",
    "Kaggle Image Dataset (200,331 samples, 16 classes, 28x28 images)",
    "Recognize handwritten digits and mathematical operators using deep learning.",
    "CNN (6 layers, BatchNorm, Dropout, Adam)",
    "Accuracy: 97.42% | F1-score: 97.42%",
    "https://handwrittendigitsandoperators-gvdahk3ls3srb5txjnkdzb.streamlit.app/"
)

project_card(
    "Speech Sentiment Analysis",
    "Kaggle Audio Dataset (MFCC, Chroma, Mel Spectrogram features)",
    "Classify speech into Positive, Neutral, or Negative sentiment.",
    "ANN vs CNN vs LSTM (Best: CNN)",
    "Best Accuracy: 86%",
    "https://dimplechouhan-speech-sentiment.hf.space"
)

project_card(
    "Disaster Risk Prediction",
    "Kaggle Tabular Dataset (20,000 records, 13 features)",
    "Predict whether a disaster is major or minor based on features like location, population affected, and economic loss.",
    "Gaussian Naive Bayes + CatBoost",
    "Accuracy: 99.95% | AUC: 99.99%",
    "https://disaster-prediction-app-rhkugqyqhucplrtq8xkhrz.streamlit.app/"
)

project_card(
    "Credit Card Fraud Detection",
    "European Card Dataset (Highly Imbalanced)",
    "Detect fraudulent transactions using imbalanced learning techniques.",
    "SMOTE + XGBoost",
    "Accuracy: 99.9% | Recall: 89.8%",
    "https://fraud-detection-app-46rkw4vsx4y5scbndpe4ff.streamlit.app/"
)

project_card(
    "Human Activity Recognition",
    "UCF101 Video Dataset (15 classes, 1500 videos)",
    "Classify human activities from video clips using deep learning.",
    "CNN + BiLSTM",
    "Accuracy: 87.33%",
    "https://huggingface.co/spaces/ArunKushwah/VisionAct_AI"
)

# ---- FOOTER ----
st.write("## 📌 About")
st.write("""
This dashboard provides access to multiple Machine Learning projects built using different types of datasets:
- Tabular Data
- Image Data
- Audio Data
- Numeric Data
- Video Data
""")
