import streamlit as st
import random

st.sidebar.title("難易度選択")
options = st.sidebar.selectbox('選択してください',['一桁×一桁','二桁×二桁','三桁×三桁'])
button_pressed = st.sidebar.button('決定')
def generate_random_multiplication_problem1(min_value1=0, max_value1=9):
    """
    Args:
    - min_value (int): 
    - max_value (int): 
    Returns:
    - problem (str): 
    - answer (int): 
    """
    num1 = random.randint(min_value1, max_value1)
    num2 = random.randint(min_value1, max_value1)
    question1 = f"{num1} × {num2}"
    answer1 = num1 * num2
    return question1, answer1
def main1():
    problem1,answer1 = generate_random_multiplication_problem1
    print(f"問題:{problem1}")
    user_answer = int(input("答えを入力してください:"))
    if user_answer == answer1:
        print("正解です")
    else:
        print(f"不正解です。正しい答えは{answer1}です。")
num3 = random.randint(10,99)
num4 = random.randint(10,99)


st.title("暗算力テスト")
st.text("１分で何問解けるかテストします")

if button_pressed:
    if options == "一桁×一桁":
       st.subheader("一桁×一桁のテスト")
       if st.button("スタート"):
        st.main1


    elif options == "二桁×二桁":
       st.subheader("二桁×二桁のテスト")
    elif options == "三桁×三桁":
       st.subheader("三桁×三桁のテスト")

