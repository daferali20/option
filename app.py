import streamlit as st
from style import load_css
from components.watchlist import watchlist_ui
from components.gainers_losers import show_gainers_losers
from components.news import show_market_news
from components.stock_news import show_stock_news
from components.prediction import show_prediction
from components.performance import show_performance
from components.analysts import show_analysts_ratings
from components.indices import show_market_indices
from components.telegram_alerts import TelegramAlerts

def setup_page():
    st.set_page_config(
        page_title="نظام مراقبة الأسهم",
        page_icon="📈",
        layout="wide"
    )
    load_css()

def sidebar():
    st.sidebar.title("القائمة الرئيسية")
    menu_options = {
        "🏠 الصفحة الرئيسية": "home",
        "📋 قائمة المراقبة": "watchlist",
        "📰 أخبار السوق": "news",
        "🚀📉 الأسهم الصاعدة والهابطة": "gainers_losers",
        "📊 أداء السهم": "performance",
        "🔮 توقعات السهم": "prediction",
        "👨‍💼 تقييم المحللين": "analysts",
        "📡 مؤشرات السوق": "indices",
        "🔔 إدارة التنبيهات": "alerts"
    }
    selected = st.sidebar.radio("اختر قسم", list(menu_options.keys()))
    return menu_options[selected]

def home_page():
    st.title("📈 نظام مراقبة الأسهم")
    st.markdown("""
    مرحباً بك في نظام مراقبة الأسهم الخاص بك. استخدم القائمة الجانبية للوصول إلى:
    - **قائمة المراقبة**
    - **أخبار السوق**
    - **الأسهم الصاعدة/الهابطة**
    - **توقعات السهم**
    """)
    col1, col2 = st.columns(2)
    with col1:
        show_market_indices(brief=True)
    with col2:
        show_gainers_losers(brief=True)

def alerts_page():
    st.title("🔔 إدارة التنبيهات")
    telegram = TelegramAlerts()
    st.subheader("إرسال تنبيه اختباري")
    if st.button("إرسال رسالة اختبارية"):
        if telegram.send_alert("🔔 هذا تنبيه اختباري من نظام مراقبة الأسهم"):
            st.success("تم إرسال التنبيه بنجاح!")
        else:
            st.error("فشل إرسال التنبيه")

def main():
    setup_page()
    page = sidebar()
    if page == "home":
        home_page()
    elif page == "watchlist":
        watchlist_ui()
    elif page == "news":
        show_market_news()
    elif page == "gainers_losers":
        show_gainers_losers()
    elif page == "performance":
        show_performance()
    elif page == "prediction":
        show_prediction()
    elif page == "analysts":
        show_analysts_ratings()
    elif page == "indices":
        show_market_indices()
    elif page == "alerts":
        alerts_page()

if __name__ == "__main__":
    main()
