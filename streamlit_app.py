import streamlit as st
import random
import time

# アプリのタイトル
st.title("掛け算タイムアタックゲーム")

# ゲームの設定
num_questions = 10

def new_question():
    """新しい掛け算の問題を生成する関数"""
    a = random.randint(10, 100)
    b = random.randint(10, 100)
    return a, b, f"{a} × {b} = ?"

def main():
    # セッションステートの初期化
    if 'start_time' not in st.session_state:
        st.session_state.start_time = None
    if 'score' not in st.session_state:
        st.session_state.score = 0
    if 'question_index' not in st.session_state:
        st.session_state.question_index = 0
    if 'a' not in st.session_state:
        st.session_state.a = None
    if 'b' not in st.session_state:
        st.session_state.b = None
    if 'current_question' not in st.session_state:
        st.session_state.current_question = ""

    # ゲームスタート
    if st.session_state.question_index == 0:
        if st.button("ゲームスタート"):
            st.session_state.start_time = time.time()
            st.session_state.score = 0
            st.session_state.question_index = 1
            st.session_state.a, st.session_state.b, st.session_state.current_question = new_question()

    # 問題が進行中
    if st.session_state.question_index > 0:
        if st.session_state.question_index <= num_questions:
            st.write(st.session_state.current_question)
            user_answer = st.text_input("答えを入力:", key=f"question_{st.session_state.question_index}")

            # 入力が正しいかどうかをチェックするボタン
            if st.button("答えをチェック", key=f"check_{st.session_state.question_index}"):
                if user_answer.isdigit() and int(user_answer) == st.session_state.a * st.session_state.b:
                    st.session_state.score += 1
                    st.success("正解！")
                else:
                    st.error("不正解！")

                # 次の問題に進む
                st.session_state.question_index += 1
                if st.session_state.question_index <= num_questions:
                    st.session_state.a, st.session_state.b, st.session_state.current_question = new_question()
                else:
                    # ゲーム終了
                    end_time = time.time()
                    elapsed_time = end_time - st.session_state.start_time
                    st.write(f"ゲーム終了！スコア: {st.session_state.score}")
                    st.write(f"所要時間: {elapsed_time:.2f}秒")
                    if st.button("再スタート"):
                        st.session_state.question_index = 0
                        st.session_state.a = None
                        st.session_state.b = None
                        st.session_state.current_question = ""

if __name__ == "__main__":
    main()
