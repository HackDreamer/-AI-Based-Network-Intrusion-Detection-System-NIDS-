import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="AI-Based Network Intrusion Detection System",
    layout="wide"
)

st.title("🔐 AI-Based Network Intrusion Detection System (NIDS)")
st.markdown("Detect malicious network traffic using Machine Learning (Random Forest).")

# -------------------------------
# Data Loading (Simulation Mode)
# -------------------------------
def load_data():
    np.random.seed(42)
    data_size = 1000

    df = pd.DataFrame({
        "packet_size": np.random.randint(40, 1500, data_size),
        "duration": np.random.uniform(0, 10, data_size),
        "src_bytes": np.random.randint(0, 10000, data_size),
        "dst_bytes": np.random.randint(0, 10000, data_size),
        "count": np.random.randint(1, 100, data_size),
        "label": np.random.choice([0, 1], data_size, p=[0.7, 0.3])  # 0 = Normal, 1 = Attack
    })
    return df

# -------------------------------
# Sidebar Controls
# -------------------------------
st.sidebar.header("⚙️ Control Panel")

if "model" not in st.session_state:
    st.session_state.model = None

if st.sidebar.button("📊 Train Model Now"):
    df = load_data()
    X = df.drop("label", axis=1)
    y = df["label"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    accuracy = accuracy_score(y_test, model.predict(X_test))

    st.session_state.model = model
    st.success(f"✅ Model trained successfully! Accuracy: {accuracy:.2f}")

# -------------------------------
# Dataset Preview
# -------------------------------
st.subheader("📁 Simulated Network Traffic Data")
df = load_data()
st.dataframe(df.head())

# -------------------------------
# Live Traffic Simulator
# -------------------------------
st.subheader("📡 Live Traffic Simulator")

col1, col2, col3 = st.columns(3)

with col1:
    packet_size = st.number_input("Packet Size", 40, 1500, 500)
    duration = st.number_input("Duration (seconds)", 0.0, 10.0, 1.0)

with col2:
    src_bytes = st.number_input("Source Bytes", 0, 10000, 2000)
    dst_bytes = st.number_input("Destination Bytes", 0, 10000, 3000)

with col3:
    count = st.number_input("Connection Count", 1, 100, 10)

if st.button("🔍 Predict Traffic Type"):
    if st.session_state.model is None:
        st.warning("⚠️ Please train the model first.")
    else:
        input_data = np.array([[packet_size, duration, src_bytes, dst_bytes, count]])
        prediction = st.session_state.model.predict(input_data)[0]

        if prediction == 0:
            st.success("🟢 Normal Traffic Detected")
        else:
            st.error("🔴 Intrusion / Attack Detected")

# -------------------------------
# Footer
# -------------------------------
st.markdown("---")
st.markdown(
    "Developed for academic demonstration of AI-based Network Intrusion Detection."
)