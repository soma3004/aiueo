# Streamlitライブラリをインポート
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

 