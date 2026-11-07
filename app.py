# HTMLコードの先頭のスペース（インデント）を削除し、改行を減らして左詰めにします
html_buttons = f"""
<div style="display: flex; flex-direction: column; gap: 30px; margin-top: 20px;">
<a href="tel:{hq_phone}" style="display: flex; align-items: center; justify-content: center; width: 100%; height: 120px; background-color: #0068c9; color: white; text-decoration: none; font-size: 26px; font-weight: bold; border-radius: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.2);">
🏢 本部へ電話
</a>
<a href="tel:{rescue_phone}" style="display: flex; align-items: center; justify-content: center; width: 100%; height: 120px; background-color: #ff4b4b; color: white; text-decoration: none; font-size: 26px; font-weight: bold; border-radius: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.2);">
🚑 救急・救護へ電話
</a>
</div>
"""

st.markdown(html_buttons, unsafe_allow_html=True)
