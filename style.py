import streamlit as st

def apply_styles():
    # مثال: تخصيص CSS للواجهة
    custom_css = """
    <style>
    /* خلفية الصفحة */
    .stApp {
        background-color: #f0f2f6;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    /* ترويسات */
    h1 {
        color: #4B7BEC;
    }
    /* النصوص */
    p, div, span {
        color: #333333;
    }
    /* زر */
    .stButton>button {
        background-color: #4B7BEC;
        color: white;
        border-radius: 8px;
        padding: 8px 16px;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #365fcf;
        color: #e0e0e0;
    }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

