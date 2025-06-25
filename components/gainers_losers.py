import streamlit as st
def show_gainers_losers(brief=False):
    if brief:
        st.subheader("🚀 أكثر الأسهم صعوداً/هبوطاً (موجز)")
    else:
        st.title("🚀📉 الأسهم الصاعدة والهابطة")
        st.write("تفاصيل كاملة لأكثر الأسهم تحركاً.")
