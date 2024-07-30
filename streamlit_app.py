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
    st.session_state.user_input = ''

# Streamlitアプリのタイトル
st.title("掛け算問題")

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

# アプリの説明
st.write("このアプリでは、ランダムに生成された掛け算の問題を解くことができます。正しい答えを入力して「答え合わせ」ボタンをクリックしてください。問題に正解すると、次の問題が表示されます。")
