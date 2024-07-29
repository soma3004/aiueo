import streamlit as st
import random

def generate_problem():
    num1 = random.randint(1, 10) 
    num2 = random.randint(1, 10)
    question = f"{num1}*{num2}"
    answer = num1*num2
    return question,answer

question,answer = generate_problem()


def check_answer(user_answer):
    return user_answer.strip() == question["answer"]

st.title("掛け算")
st.write(f"計算式:{question}")
user_input = st.text_input("式の答えを入力してください。")

if st.button("答え合わせ"):
    if user_input:
        if check_answer(user_input):
            st.success("正解です！")
        else:
            st.error("不正解です。、もう一度試してみてください。")
    else:
        st.warning("回答を入力してください。")

        