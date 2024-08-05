import streamlit as st
import random
def generate_random_multiplication_problem1():
    a = random.randint(1,9)
    b = random.randint(1,9)
    question1 = f"{a} × {b}"
    answer1 = a * b
    return question1,answer1
options = ["一桁×一桁","二桁×二桁","三桁×三桁"]
selected_option = st.selectbox("難易度を選んでください",options)
if selected_option == "一桁×一桁":
    st.subheader("一桁×一桁")
    if st.button("スタート"):
        question, answer = generate_random_multiplication_problem1()
        st.write(f"問題:{question}")
        user_answer = st.number_input("答えを入力してください")
        if st.button("答え合わせ"):
            if user_answer == answer:
                st.success("正解です！")
            else:
                st.error("不正解です。")

    
