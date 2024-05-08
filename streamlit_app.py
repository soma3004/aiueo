# Streamlitライブラリをインポート
import streamlit as st

st.title("bmi計算アプリ")


flgcheck_A = st.checkbox('checkbox A')
flgcheck_B = st.checkbox('checkbox B')

flgcheck_A
st.text('checkbox A has checed')
flgcheck_B
st.text('checkbox B has checked')