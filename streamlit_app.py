import streamlit as st
import random

st.sidebar.title("難易度選択")
options = st.sidebar.selectbox('選択してください', ['一桁×一桁', '二桁×二桁', '三桁×三桁'])
button_pressed = st.sidebar.button('決定')

def generate_random_multiplication_problem(min_value1, max_value1):
    num1 = random.randint(min_value1, max_value1)
    num2 = random.randint(min_value1, max_value1)
    question = f"{num1} × {num2}"
    answer = num1 * num2
    return question, answer

st.title("暗算力テスト")
st.text("１分で何問解けるかテストします")

if button_pressed:
    if options == "一桁×一桁":
        st.subheader("一桁×一桁のテスト")
        
        question, answer = generate_random_multiplication_problem(0, 9)
        
        st.write(f"問題: {question}")
        
        user_answer = st.number_input("答えを入力してください:")
        
        if st.button("答えをチェック"):
            if user_answer == answer:
                st.success("正解です！")
            else:
                st.error(f"不正解です。正しい答えは {answer} です。")

    elif options == "二桁×二桁":
        st.subheader("二桁×二桁のテスト")
        question, answer = generate_random_multiplication_problem(10, 99)
        st.write(f"問題: {question}")
        user_answer = st.number_input("答えを入力してください:", min_value=0, step=1)
        if st.button("答えをチェック"):
            if user_answer == answer:
                st.success("正解です！")
            else:
                st.error(f"不正解です。正しい答えは {answer} です。")
                
    elif options == "三桁×三桁":
        st.subheader("三桁×三桁のテスト")
        question, answer = generate_random_multiplication_problem(100, 999)
        st.write(f"問題: {question}")
        user_answer = st.number_input("答えを入力してください:", min_value=0, step=1)
        if st.button("答えをチェック"):
            if user_answer == answer:
                st.success("正解です！")
            else:
                st.error(f"不正解です。正しい答えは {answer} です。")
