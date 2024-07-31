import streamlit as st
import random
import time

# アプリのタイトル
st.title("掛け算タイムアタックゲーム")

# ゲームの設定
num_questions = 10
score = 0
question_index = 0
start_time = None

def new_question():
    """新しい掛け算の問題を生成する関数"""
    global a, b
    a = random.randint(1, 9)
    b = random.randint(1, 9)
    return f"{a} × {b} = ?"

def check_answer(answer):
    """ユーザーの答えをチェックする関数"""
    global score, question_index
    if int(answer) == a * b:
        score += 1
        question_index += 1
        return True
    else:
        question_index += 1
        return False

def main():
    global start_time
    
    if "start_time" not in st.session_state:
        st.session_state.start_time = None
    if "score" not in st.session_state:
        st.session_state.score = 0
    if "question_index" not in st.session_state:
        st.session_state.question_index = 0

    if st.session_state.question_index == 0 and st.button("ゲームスタート"):
        st.session_state.start_time = time.time()
        st.session_state.score = 0
        st.session_state.question_index = 1

    if st.session_state.question_index > 0:
        if st.session_state.question_index <= num_questions:
            question = new_question()
            user_answer = st.text_input(question, key=f"question_{st.session_state.question_index}")
            
            if st.button("答えをチェック"):
                if check_answer(user_answer):
                    st.success("正解！")
                else:
                    st.error("不正解！")
                    
            st.write(f"現在のスコア: {st.session_state.score}")
        else:
            end_time = time.time()
            elapsed_time = end_time - st.session_state.start_time
            st.write(f"ゲーム終了！スコア: {st.session_state.score}")
            st.write(f"所要時間: {elapsed_time:.2f}秒")
            if st.button("再スタート"):
                st.session_state.question_index = 0

if __name__ == "__main__":
    main()
