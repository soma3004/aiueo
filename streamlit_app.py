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

def complete_square(a, b, c):
    alpha = -b / (2 * a)
    beta = c - (b**2 / (4 * a))
    return alpha, beta

def solve_quadratic(a, b, c):
    alpha, beta = complete_square(a, b, c)
    if beta < 0:
        root1 = complex(alpha + cmath.sqrt(beta))
        root2 = complex(alpha - cmath.sqrt(beta))
    else:
        root1 = alpha + cmath.sqrt(beta)
        root2 = alpha - cmath.sqrt(beta)
    return root1, root2

def main():
    st.title('二次方程式の解を計算するアプリ')

    a = st.number_input('二次の係数 a を入力してください', step=1.0)
    b = st.number_input('一次の係数 b を入力してください', step=1.0)
    c = st.number_input('定数項 c を入力してください', step=1.0)

    if st.button('計算'):
        if a != 0:
            root1, root2 = solve_quadratic(a, b, c)
            st.success(f'解は {root1} と {root2} です。')
        else:
            st.error('二次の係数 a は0ではない値を入力してください。')

if __name__ == '__main__':
    main()
