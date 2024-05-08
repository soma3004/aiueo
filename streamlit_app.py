# Streamlitライブラリをインポート
import streamlit as st

selected_item = st.selectbox('select item',['A','B','C'])

st.text(selected_item)

selected_item = st.selectbox('select_item',['A'],['B'],['c'], index=2)

st.text('selected_item')