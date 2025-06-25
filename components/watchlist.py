import sqlite3
import streamlit as st
from config import DB_PATH
from utils.helpers import validate_symbol

class Watchlist:
    def __init__(self):
        self.conn = sqlite3.connect(DB_PATH)
        self._create_table()

    def _create_table(self):
        """إنشاء جدول Watchlist إذا لم يكن موجودًا"""
        query = """
        CREATE TABLE IF NOT EXISTS watchlist (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            symbol TEXT NOT NULL UNIQUE,
            added_date TEXT DEFAULT CURRENT_TIMESTAMP
        )
        """
        self.conn.execute(query)
        self.conn.commit()

    def add_stock(self, symbol):
        """إضافة سهم إلى قائمة المراقبة"""
        if not validate_symbol(symbol):
            return False, "رمز السهم غير صالح"
        
        try:
            self.conn.execute("INSERT INTO watchlist (symbol) VALUES (?)", (symbol.upper(),))
            self.conn.commit()
            return True, f"تمت إضافة {symbol} إلى قائمة المراقبة بنجاح"
        except sqlite3.IntegrityError:
            return False, f"{symbol} موجود بالفعل في قائمة المراقبة"

    def remove_stock(self, symbol):
        """إزالة سهم من قائمة المراقبة"""
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM watchlist WHERE symbol = ?", (symbol.upper(),))
        self.conn.commit()
        if cursor.rowcount > 0:
            return True, f"تمت إزالة {symbol} من قائمة المراقبة"
        return False, f"{symbol} غير موجود في قائمة المراقبة"

    def get_watchlist(self):
        """استرجاع قائمة المراقبة كقائمة"""
        cursor = self.conn.cursor()
        cursor.execute("SELECT symbol FROM watchlist ORDER BY added_date DESC")
        return [row[0] for row in cursor.fetchall()]

    def __del__(self):
        """إغلاق الاتصال عند التدمير"""
        self.conn.close()

# واجهة Streamlit لإدارة قائمة المراقبة
def watchlist_ui():
    st.header("📋 قائمة مراقبة الأسهم")
    watchlist = Watchlist()
    
    # قسم الإضافة
    with st.form("add_form"):
        col1, col2 = st.columns([3, 1])
        symbol = col1.text_input("أدخل رمز السهم (مثال: AAPL, TSLA)", key="wl_input")
        submitted = col2.form_submit_button("إضافة")
        
        if submitted and symbol:
            success, message = watchlist.add_stock(symbol.strip())
            if success:
                st.success(message)
            else:
                st.error(message)
    
    # عرض قائمة المراقبة
    st.subheader("أسهمك المتابعة")
    stocks = watchlist.get_watchlist()
    
    if not stocks:
        st.info("لا توجد أسهم في قائمة المراقبة. أضف بعض الأسهم باستخدام النموذج أعلاه.")
    else:
        for stock in stocks:
            col1, col2 = st.columns([4, 1])
            col1.write(f"📌 {stock}")
            if col2.button("حذف", key=f"del_{stock}"):
                _, message = watchlist.remove_stock(stock)
                st.experimental_rerun()  # إعادة تحميل الواجهة

# اختبار الوحدة
if __name__ == "__main__":
    watchlist_ui()
