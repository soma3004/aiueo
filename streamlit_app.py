import streamlit as st
import random
import numpy as np

def generate_quadratic_equation():
    a = random.randint(1,10) * random.choice([1,2])
    b = random.randint(1, 10) * random.choice([1,2])
    c = random.randint(1, 10) * random.choice([1,2])
    return a, b, c

problem = {
    "question":"a × b",
    "answer":"ab"
}

def check_answer(user_answer):
    return user_answer.strip() == problem["answer"]

st.title("掛け算")
st.write(problem["question"])
user_input = st.text_input("式の答えを入力してください。")

if st.button("答え合わせ"):
    if user_input:
        if check_answer(user_input):
            st.success("正解です！")
        else:
            st.error("不正解です。、もう一度試してみてください。")
    else:
        st.warning("回答を入力してください。")
        
        