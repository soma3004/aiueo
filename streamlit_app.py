import streamlit as st
import random

st.sidebar.title("難易度選択")
options = st.sidebar.selectbox('選択してください', ['一桁×一桁', '二桁×二桁', '三桁×三桁'])
button_pressed = st.sidebar.button('決定')

def generate_random_multiplication_problem(min_value1, max_value1):
    num1 = random.randint(min_value1, max_value1)
    num2 = random.randint(min_value1, max_value1)
    question = f"{num1} × {num2}"
    answer = num1 * num2
    return question, answer

st.title("暗算力テスト")
st.text("１分で何問解けるかテストします")

if button_pressed:
    if options == "一桁×一桁":
        st.subheader("一桁×一桁のテスト")
        
        question, answer = generate_random_multiplication_problem(0, 9)
        
        st.write(f"問題: {question}")
        
        col1, col2, col3 = st.columns(3)
    with col1:
        if st.button('1'):
            st.session_state.user_answer += '1'
        if st.button('4'):
            st.session_state.user_answer += '4'
        if st.button('7'):
            st.session_state.user_answer += '7'
        if st.button('C'):
            st.session_state.user_answer = ''
    
    with col2:
        if st.button('2'):
            st.session_state.user_answer += '2'
        if st.button('5'):
            st.session_state.user_answer += '5'
        if st.button('8'):
            st.session_state.user_answer += '8'
        if st.button('0'):
            st.session_state.user_answer += '0'
    
    with col3:
        if st.button('3'):
            st.session_state.user_answer += '3'
        if st.button('6'):
            st.session_state.user_answer += '6'
        if st.button('9'):
            st.session_state.user_answer += '9'
        if st.button('Enter'):
            st.session_state.checked = True

    st.write(f"入力された答え: {st.session_state.user_answer}")

    # チェックボタン
    if st.session_state.checked:
        if st.session_state.user_answer.isdigit():
            if int(st.session_state.user_answer) == st.session_state.answer:
                st.success("正解です！")
            else:
                st.error(f"不正解です。正しい答えは {st.session_state.answer} です。")
        else:
            st.error("無効な入力です。数字のみを入力してください。")
    elif options == "二桁×二桁":
        st.subheader("二桁×二桁のテスト")
        question, answer = generate_random_multiplication_problem(10, 99)
        st.write(f"問題: {question}")
        user_answer = st.number_input("答えを入力してください:", min_value=0, step=1)
        if st.button("答えをチェック"):
            if user_answer == answer:
                st.success("正解です！")
            else:
                st.error(f"不正解です。正しい答えは {answer} です。")
                
    elif options == "三桁×三桁":
        st.subheader("三桁×三桁のテスト")
        question, answer = generate_random_multiplication_problem(100, 999)
        st.write(f"問題: {question}")
        user_answer = st.number_input("答えを入力してください:", min_value=0, step=1)
        if st.button("答えをチェック"):
            if user_answer == answer:
                st.success("正解です！")
            else:
                st.error(f"不正解です。正しい答えは {answer} です。")