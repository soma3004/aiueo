import streamlit as st
import random

def hannbetusiki():
    b,c,a=random.sample(range(1,100),3)
    b,c,a=sorted([b,c,a], reverse=True)
    
    st.write(f"a={a},b={b},c={c}")
    
hannbetusiki()
    
