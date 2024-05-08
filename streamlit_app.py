# Streamlitライブラリをインポート
import streamlit as st

st.title("bmi計算アプリ")
st.write("体重を入力してください")

weight = st.number_input("体重を入力",min_value=1.0)

height = st.number_input("身長を入力",min_value=1.0)

bmi = weight/(height*height)
st.write("あなたのbmiは"+str(bmi)+"です")