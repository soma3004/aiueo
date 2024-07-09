# Streamlitライブラリをインポート
# app.py

# math_quiz_app.py

# app.py

import streamlit as st
import random

def generate_question():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    return num1, num2

def main():
    st.title('足し算問題')
    st.write('以下の問題に答えてください：')

    num1, num2 = generate_question()

    answer = st.text_input(f'{num1} + {num2} =', '')

    if answer:
        try:
            user_answer = int(answer)
            correct_answer = num1 + num2
            if user_answer == correct_answer:
                st.write('正解です！')
            else:
                st.write(f'不正解です。正解は {correct_answer} です。')
        except ValueError:
            st.write('数値を入力してください。')

if __name__ == '__main__':
    main()
