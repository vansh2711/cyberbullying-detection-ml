import streamlit as st
import pickle

# ==========================================
# CONFIG
# ==========================================
MODEL_PATH = "cyberbullying_model.pkl"

st.set_page_config(
    page_title="Cyberbullying Detector",
    page_icon="🛡️",
    layout="wide"
)

# ==========================================
# LOAD MODEL
# ==========================================
@st.cache_resource
def load_model():
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
    return model

# Try loading model
try:
    model = load_model()
    model_loaded = True
except FileNotFoundError:
    st.error("❌ Model file not found! Please keep 'cyberbullying_model.pkl' in the same folder.")
    model_loaded = False

# ==========================================
# UI DESIGN
# ==========================================
st.title("🛡️ Cyberbullying Detection System")
st.markdown("Detect harmful or offensive content in real-time using Machine Learning.")

st.divider()

# Input Section
st.subheader("✍️ Enter Tweet Text")
user_input = st.text_area("Type or paste a tweet below:", height=150)

# ==========================================
# PREDICTION
# ==========================================
if st.button("🚀 Classify Tweet"):

    if not model_loaded:
        st.error("Model not loaded. Please check file.")
    
    elif not user_input.strip():
        st.info("⚠️ Please enter some text first.")
    
    else:
        with st.spinner("🔍 Analyzing..."):
            prediction = model.predict([user_input])[0]

        st.subheader("📊 Result")

        if prediction == "not_cyberbullying":
            st.success("✅ SAFE CONTENT")
        else:
            st.error(f"⚠️ {prediction.upper()} DETECTED")

        st.caption(f"Model Output: {prediction}")

st.divider()

# Footer
st.markdown("👨‍💻 Developed by Vansh Patel | ML Internship Project")