import streamlit as st

# ページ設定
st.set_page_config(page_title="緊急連絡アプリ", page_icon="🚑", layout="centered")

# ==========================================
# 1. ログイン認証の仕組み
# ==========================================
# セッションステート（状態保存）の初期化
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

def check_password():
    """入力されたパスワードが正しいかチェックする関数"""
    try:
        # 入力されたパスワードとsecretsのパスワードを比較
        if st.session_state["password_input"] == st.secrets["APP_PASSWORD"]:
            st.session_state["authenticated"] = True
            st.session_state.pop("password_error", None) # エラー表示を消す
        else:
            st.session_state["authenticated"] = False
            st.session_state["password_error"] = True
    except KeyError:
        st.error("エラー: パスワードが設定されていません。管理者に連絡してください。")
        st.stop()

# ログインしていない場合はログイン画面を表示
if not st.session_state["authenticated"]:
    st.title("🔒 ログイン")
    st.write("運営用アプリです。パスワードを入力してください。")
    
    # パスワード入力欄（入力されると check_password が実行される）
    st.text_input("パスワード", type="password", key="password_input", on_change=check_password)
    
    # 間違えた場合のエラーメッセージ
    if st.session_state.get("password_error"):
        st.error("パスワードが間違っています。")
    
    # ここで処理を止めて、下の連絡網を表示させない！
    st.stop()


# ==========================================
# 2. メイン画面（ログイン成功後のみ表示される）
# ==========================================
st.title("🏃‍♂️ リレーマラソン 緊急連絡網")
st.info("緊急事態が発生した場合は、以下のボタンから各担当へ電話を発信してください。")

try:
    hq_phone = st.secrets["HQ_PHONE"]
    rescue_phone = st.secrets["RESCUE_PHONE"]
except KeyError:
    st.error("エラー: 電話番号が設定されていません。管理者に連絡してください。")
    st.stop()

# 本部への連絡セクション
st.subheader("🏢 大会本部")
st.write("コース上のトラブル、備品不足、その他運営に関する報告はこちら")
st.link_button("📞 本部に電話をかける", f"tel:{hq_phone}", type="primary", use_container_width=True)

st.divider()

# 救急・救護への連絡セクション
st.subheader("🚑 救急・救護")
st.write("ケガ人や体調不良者の発生など、医療処置が必要な場合はこちら")
st.link_button("📞 救急・救護に電話をかける", f"tel:{rescue_phone}", type="primary", use_container_width=True)
