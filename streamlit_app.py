import streamlit as st
import random

options = ["一桁×一桁","二桁×二桁","三桁×三桁"]
selected_option = st.selectbox("難易度を選んでください",options)
if selected_option == "一桁×一桁":
    st.subheader("一桁×一桁")
    st.button("スタート")
