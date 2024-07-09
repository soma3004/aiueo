# Streamlitライブラリをインポート
# app.py

import streamlit as st

def main():
    st.title('数学')
    st.write('公式')

    # 例: ユーザーに名前を入力してもらう
    username = st.text_input('あなたの名前を入力してください')

 