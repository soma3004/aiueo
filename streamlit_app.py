# Streamlitライブラリをインポート
# app.py

# math_quiz_app.py

# app.py

import streamlit as st
import random

def generate_question():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
   
def main():
    st.title('問題')
    st.write('以下の問題に答えてください：')

    num1, num2 = generate_question()

    answer = st.text_input(f'{num1} + {num2} =', '')

   

if __name__ == '__main__':
    main()
