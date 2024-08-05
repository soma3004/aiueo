import streamlit as st

st.sidebar.title("難易度選択")
options = st.sidebar.selectbox('選択してください',['一桁×一桁','二桁×二桁','三桁×三桁'])



st.title("暗算力テスト")
st.text("１分で何問解けるかテストします")

if st.button("決定"):
    if options == "一桁×一桁":
       st.title("一桁×一桁")
    elif options == "二桁×二桁":
       st.title("二桁×二桁")
    elif options == "三桁×三桁":
       st.title("三桁×三桁")

