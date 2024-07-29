import streamlit as st
import random
import numpy as np

def generate_quadratic_equation():
    a = random.randint(1,10) * random.choice([1,2])
    b = random.randint(1, 10) * random.choice([1,2])
    c = random.randint(1, 10) * random.choice([1,2])
    return a, b, c

problem = {
    "question":"a × b",
    "answer":"ab"
    

}