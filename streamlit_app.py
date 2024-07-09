# Streamlitライブラリをインポート
# app.py

# math_quiz_app.py

import streamlit as st
import random

def generate_question():
    """ランダムな数学の問題を生成する関数"""
    num1= random.randint(-100,100)
    num2 = random.randint(-100,100)
    operator = random.choice(['+', '-', '*'])
    
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    elif operator == '*':
        answer = num1 * num2
    
    return num1, num2, operator, answer

    if st.button('答え合わせ')：
        if st.wite(answer):
            