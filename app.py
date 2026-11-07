import streamlit as st

# ページ設定
st.set_page_config(page_title="緊急連絡", page_icon="🚑", layout="centered")

# ==========================================
# 1. ログイン認証
# ==========================================
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

def check_password():
    try:
        if st.session_state["password_input"] == st.secrets["APP_PASSWORD"]:
            st.session_state["authenticated"] = True
            st.session_state.pop("password_error", None)
        else:
            st.session_state["authenticated"] = False
            st.session_state["password_error"] = True
    except KeyError:
        st.error("エラー: パスワード未設定")
        st.stop()

if not st.session_state["authenticated"]:
    st.text_input("🔑 パスワード", type="password", key="password_input", on_change=check_password)
    if st.session_state.get("password_error"):
        st.error("パスワードが違います")
    st.stop()

# ==========================================
# 2. メイン画面（巨大ボタンのみ）
# ==========================================
try:
    hq_phone = st.secrets["HQ_PHONE"]
    rescue_phone = st.secrets["RESCUE_PHONE"]
except KeyError:
    st.error("エラー: 電話番号未設定")
    st.stop()

# HTML/CSSでスマホ向けに最適化した巨大ボタンを作成
html_buttons = f"""
<div style="display: flex; flex-direction: column; gap: 30px; margin-top: 20px;">
    <a href="tel:{hq_phone}" 
       style="display: flex; align-items: center; justify-content: center; width: 100%; height: 120px; 
              background-color: #0068c9; color: white; text-decoration: none; 
              font-size: 26px; font-weight: bold; border-radius: 15px; 
              box-shadow: 0 4px 6px rgba(0,0,0,0.2);">
        🏢 本部へ電話
    </a>
    
    <a href="tel:{rescue_phone}" 
       style="display: flex; align-items: center; justify-content: center; width: 100%; height: 120px; 
              background-color: #ff4b4b; color: white; text-decoration: none; 
              font-size: 26px; font-weight: bold; border-radius: 15px; 
              box-shadow: 0 4px 6px rgba(0,0,0,0.2);">
        🚑 救急・救護へ電話
    </a>
</div>
"""

st.markdown(html_buttons, unsafe_allow_html=True)
