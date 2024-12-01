import streamlit as st
import random

def hannbetusiki():
    a,c,b=random.sample(range(1,100),3)
    a,c,b=sorted([a,c,b], reverse=True)
    print(a,b,c)
    
hannbetusiki()
    
