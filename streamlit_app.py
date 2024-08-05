
import streamlit as st
import random

# サイドバーで難易度を選択
st.sidebar.title("難易度選択")
options = st.sidebar.selectbox('選択してください', ['一桁×一桁', '二桁×二桁', '三桁×三桁'])
button_pressed = st.sidebar.button('決定')

# 問題生成関数
def generate_random_multiplication_problem(min_value1, max_value1):
    num1 = random.randint(min_value1, max_value1)
    num2 = random.randint(min_value1, max_value1)
    question = f"{num1} × {num2}"
    answer = num1 * num2
    return question, answer

# メインアプリの構成
st.title("暗算力テスト")
st.text("１分で何問解けるかテストします")

# 初期状態設定
if 'question' not in st.session_state:
    st.session_state.question = None
    st.session_state.answer = None
    st.session_state.user_answer = None
    st.session_state.checked = False

# ボタンが押された時の処理
if button_pressed:
    if options == "一桁×一桁":
        st.subheader("一桁×一桁のテスト")
        
        # 一桁×一桁の問題を生成
        st.session_state.question, st.session_state.answer = generate_random_multiplication_problem(0, 9)
        st.session_state.checked = False

    elif options == "二桁×二桁":
        st.subheader("二桁×二桁のテスト")
        
        # 二桁×二桁の問題を生成
        st.session_state.question, st.session_state.answer = generate_random_multiplication_problem(10, 99)
        st.session_state.checked = False

    elif options == "三桁×三桁":
        st.subheader("三桁×三桁のテスト")
        
        # 三桁×三桁の問題を生成
        st.session_state.question, st.session_state.answer = generate_random_multiplication_problem(100, 999)
        st.session_state.checked = False

# 問題文と解答チェック
if st.session_state.question:
    st.write(f"問題: {st.session_state.question}")

    # ユーザーの解答入力フィールド
    st.session_state.user_answer = st.number_input("答えを入力してください:", min_value=0, step=1, key="user_answer")
    
    # チェックボタン
    if st.button("答えをチェック"):
        st.session_state.checked = True
    
    if st.session_state.checked:
        if st.session_state.user_answer == st.session_state.answer:
            st.success("正解です！")
        else:
            st.error(f"不正解です。正しい答えは {st.session_state.answer} です。")
