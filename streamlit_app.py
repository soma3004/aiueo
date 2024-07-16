import streamlit as st
import random
import numpy as np

def generate_quadratic_equation():
    a = random.randint(1,10) * random.choice([0,2])
    b = random.randint(1, 10) * random.choice([0,2])
    c = random.randint(1, 10) * random.choice([0,2])
    return a, b, c

def main():
    st.title('')
    st.write('以下の二次方程式の解の個数を求めてください：')

    a, b, c = generate_quadratic_equation()

    st.latex(f"{a}x^2 + {b}x + {c} = 0")

    st.write('解を入力してください：')
    answer = st.text_input('', '','個')

    if answer:
        try:
            user_answer = float(answer)
            # Solve the quadratic equation
            discriminant = b**2 - 4*a*c
            if discriminant < 0:
                st.write('実数解はありません。')
            else:
                sqrt_discriminant = np.sqrt(discriminant)
                x1 = (-b + sqrt_discriminant) / (2*a)
                x2 = (-b - sqrt_discriminant) / (2*a)

                if np.isclose(user_answer, x1) or np.isclose(user_answer, x2):
                    st.write('正解です！')
                else:
                    st.write('不正解です。')
                    st.write(f'正解は x = {x1} または x = {x2} です。')
        except ValueError:
            st.write('数値を入力してください。')

if __name__ == '__main__':
    main()
