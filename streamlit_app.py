import streamlit as st
import random

def hannbetusiki():
    b,c,a=random.sample(range(1,100),3)
    b,c,a=sorted([b,c,a], reverse=True)
    A=str(a)+"x^2"
    B=str(b)+"x"
    C=str(c)
    st.latex(A+B+C)
hannbetusiki()
    
