import streamlit as st
import random
import numpy as np

def generate_quadratic_equation():
    a = random.randint(1,10) * random.choice([1,2])
    b = random.randint(1, 10) * random.choice([1,2])
    c = random.randint(1, 10) * random.choice([1,2])
    return a, b, c

def main():
    st.title('')
    st.write('以下の二次方程式の解の個数を求めてください：')

    a, b, c = generate_quadratic_equation()

    st.latex(f"{a}x^2 + {b}x + {c} = 0")

    st.write('解の個数を入力してください：')
    answer = st.text_input("")

    

    if answer:
        try:
            discriminant = b**2 - 4*a*c
            if discriminant < 0:
                st.write('実数解は0個です。')
            elif discriminant == 0: # type: ignore
                st.write('実数解は1個です。')
            else:
                discriminant > 0
                st.write('実数解は2個です。')
            
                
        except ValueError:
            st.write('数値を入力してください。')

