import streamlit as st
import random

# 問題数の設定
NUM_PROBLEMS = 100

# セッション状態を利用して現在の問題インデックスと問題を保持
if 'current_problem_index' not in st.session_state:
    st.session_state.current_problem_index = 0

if 'problems' not in st.session_state:
    st.session_state.problems = [(random.randint(10, 100), random.randint(10, 100)) for _ in range(NUM_PROBLEMS)]

if 'user_input' not in st.session_state:
    st.session_state.user_input = ''

if 'current_answer' not in st.session_state:
    # 問題の最初の答えをセットアップする
    current_problem = st.session_state.problems[st.session_state.current_problem_index]
    st.session_state.current_answer = current_problem[0] * current_problem[1]

def check_answer(user_answer):
    return user_answer.strip() == str(st.session_state.current_answer)

def next_problem():
    if st.session_state.current_problem_index < len(st.session_state.problems) - 1:
        st.session_state.current_problem_index += 1
    else:
        st.session_state.current_problem_index = 0

    # 次の問題の答えをセットアップする
    current_problem = st.session_state.problems[st.session_state.current_problem_index]
    st.session_state.current_answer = current_problem[0] * current_problem[1]

    # ユーザーの入力をリセットする
    st.session_state.user_input = ""

# Streamlitアプリのタイトル
st.title("")

# 現在の問題を取得
current_problem = st.session_state.problems[st.session_state.current_problem_index]
a, b = current_problem

# 問題を表示
st.write(f"{a} × {b} = ?")

# ユーザーの入力を受け取る
user_input = st.text_input("答えを入力してください:", key="user_input")

# 正誤判定とフィードバック
if st.button("答え合わせ"):
    if user_input:
        if check_answer(user_input):
            st.success("正解です！")
            next_problem()
        else:
            st.error("不正解です。もう一度試してみてください。")
    else:
        st.warning("回答を入力してください。")

# 次の問題に進むためのボタン
if st.button("次の問題"):
    next_problem()

import streamlit as st

def continued_fraction(p, q):
    a_list = []
    while q != 0:
        a = p // q
        a_list.append(a)
        p, q = q, p - a * q
    return a_list

def approximate_fraction(p, q, n):
    a_list = continued_fraction(p, q)
    approx = a_list[0]
    for i in range(1, n):
        approx = a_list[i] + 1 / approx
    return approx

def main():
    st.title('分数の近似値計算')

    numerator = st.number_input('分子を入力してください', min_value=1, step=1)
    denominator = st.number_input('分母を入力してください', min_value=1, step=1)
    approximations = st.number_input('近似の反復回数を入力してください', min_value=1, step=1)

    if st.button('計算'):
        if numerator and denominator and approximations:
            approx_value = approximate_fraction(numerator, denominator, int(approximations))
            st.success(f"分数 {numerator}/{denominator} の近似値は {approx_value:.8f}")

if __name__ == '__main__':
    main()
