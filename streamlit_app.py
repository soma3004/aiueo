import streamlit as st
import random
b=random.sample(range(25,50),1)
c,a=random.sample(range(1,25),2)
c,a=sorted([c,a], reverse=True)


def hannbetusiki():
    A=str(a)+"x^2"
    B=str(b)+"x"
    C=str(c)
    st.latex(A+"+"+B+"+"+C)

def answer():
    st.write("この2次方程式には解が何個ありますか。")
    kai=b*b-4*a*c
    if kai > 0:
        kosuu=2
    elif kai < 0:
        kosuu=0
    else:
        kosuu=1
    st.write("答えは"+str(kosuu)+"個です。")

hannbetusiki()
answer()

    
