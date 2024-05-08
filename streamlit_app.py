# Streamlitライブラリをインポート
import streamlit as st

st.title("bmi計算アプリ")
st.write("体重を入力してください")

weight = st.number_input("体重を入力")

height = st.number_input("身長を入力")

bmi = weight/(height*height)
st.write("あなたのbmiは"+str(bmi)+"kgです")