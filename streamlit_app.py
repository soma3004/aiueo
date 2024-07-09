# Streamlitライブラリをインポート
# app.py

import streamlit as st

def main():
    st.title('数学計算')
    st.write('あ')

    # 例: ユーザーに名前を入力してもらう
    username = st.text_input('あなたの名前を入力してください')

# app.py

import streamlit as st

def main():
    st.title('スタート画面')

    menu = ['ホーム', '設定']
    choice = st.sidebar.selectbox('メニュー', menu)

    if choice == 'ホーム':
        show_homepage()
    elif choice == '設定':
        show_settings()

def show_homepage():
    st.title('ホームページ')
    st.write('ここはホームページです。')

def show_settings():
    st.title('設定')
    st.write('ここは設定ページです。')

if __name__ == '__main__':
    main()

 