import streamlit as st


st.title("暗算力テスト")
st.text("１分で何問解けるかテストします")
options = ["一桁×一桁","二桁×二桁","三桁×三桁"]
selected_option = st.selectbox("挑戦する内容を選んでください。",options)

if selected_option == "一桁×一桁":
    st.title("一桁×一桁")
elif selected_option == "二桁×二桁":
    st.title("二桁×二桁")
elif selected_option == "三桁×三桁":
    st.title("三桁×三桁")

