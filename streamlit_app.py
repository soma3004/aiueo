import streamlit as st

st.sidebar.title("難易度選択")
options = st.sidebar.selectbox('選択してください',['一桁×一桁','二桁×二桁','三桁×三桁'])
button_pressed = st.sidebar.button('決定')


st.title("暗算力テスト")
st.text("１分で何問解けるかテストします")

if button_pressed:
    if options == "一桁×一桁":
       st.header("一桁×一桁のテスト")
    elif options == "二桁×二桁":
       st.header("二桁×二桁のテスト")
    elif options == "三桁×三桁":
       st.header("三桁×三桁のテスト")

