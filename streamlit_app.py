# Streamlitライブラリをインポート
# app.py

# math_quiz_app.py

import streamlit as st
import random

def generate_question():
    """ランダムな数学の問題を生成する関数"""
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operator = random.choice(['+', '-', '*'])
    
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    elif operator == '*':
        answer = num1 * num2
    
    return num1, num2, operator, answer

def main():
    st.title('数学の問題を解こう！')

    num1, num2, operator, answer = generate_question()

    user_answer = st.number_input(f'{num1} {operator} {num2} = ', min_value=-100, max_value=100, key='user_answer')

    if st.button('答えをチェック'):
        if user_answer == answer:
            st.success('正解です！ 🎉')
        else:
            st.error(f'不正解です。正解は {answer} です。 😞')

    st.write('---')
    st.write('新しい問題を解く準備ができたら、再度「答えをチェック」ボタンを押してください。')

if __name__ == '__main__':
    main()


