import streamlit as st
import random

def hannbetusiki():
    a,c,b=random.sample(range(1,100),3)
    a,c,b=sorted([a,c,b], reverse=True)
    
    st.print(f"a={a},b={b},c={c}")
    
hannbetusiki()
    
