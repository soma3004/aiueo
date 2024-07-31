import streamlit as st
import random
import time

st.title("計算力テスト")
game_duration = 30

def new_question():
    a = random.randint(10,100)
    b = random.randint(10,100)
    return a,b,f"{a}×{b} = ?"

def main():
    if 'start_time'not in st.session_state:
        st.session_state.start_time = None
    if 'score' not in st.session_state:
        st.session_state.score = 0
    if 'current_question' not in st.session_state:
        st.session_state.current_question = ""
    if 'a' not in st.session_state:
        st.session_state.a = None
    if 'b' not in st .session_state:
        st.session_state.b = None
    if 'ganme_active' not in st.session_state:
        st.session_state.game_active = False
    
    if not st.session_state.game_active:
        if st.button("ゲームスタート"):
            st.session_state.start_time = time.time()
            st.session_state.score = 0
            st.session_state.current_question = ""
            st.session_state.a, st.session_state.b, st.session_state.current_question = new_question()
            st.session_state.game_active = True

    if st.session_state.game_active:
        elapsed_time = time.time() -  st.session_state.start_time

        if elapsed_time < game_duration:
            st.write(st.session_state.current_question)
            user_answer = st.text_input("答えを入力:",key="user_answer")
            st.session_state.user_answer = user_answer

            if st.button("答えをチェック"):
                if user_answer.isdigit() and int(user_answer) == st.session_a * st.session.sesion_state.b:
                    st.session_state.score += 1
                    st.success("正解！")
                else:
                    st.error("不正解！")
                st.session_state.a, st.session_state.b, st.session_state.current_question = new_question()
                st.session_state.user_answer = ""
            st.write(f"現在のスコア：{st.session_state.score}")
            st.write(f"残り時間: {max(0, game_duration - int(elapsed_time))}秒")

        else:    
            st.write(f"ゲーム終了！スコア: {st.session_state.scoere}")
            if st.button("再スタート"):
                st.session_state.game_active = False
                st.session_state.user_answer = ""

if __name__ == "__main__":
    main()
