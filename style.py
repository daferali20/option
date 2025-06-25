import streamlit as st

def load_css():
    custom_css = """
    <style>
    .stApp {
        background-color: #f8f9fa;
        font-family: 'Segoe UI', sans-serif;
    }
    h1, h2, h3 {
        color: #1f77b4;
    }
    .stButton>button {
        background-color: #1f77b4;
        color: white;
        border-radius: 5px;
        padding: 8px 16px;
    }
    .stButton>button:hover {
        background-color: #105c91;
    }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)
