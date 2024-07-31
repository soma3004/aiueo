import streamlit as st
import random
import time

# アプリのタイトル
st.title("30秒タイムアタックゲーム")

# ゲームの設定
game_duration = 30  # ゲームの制限時間（秒）

def new_question():
    """新しい掛け算の問題を生成する関数"""
    a = random.randint(1, 9)
    b = random.randint(1, 9)
    return a, b, f"{a} × {b} = ?"

def main():
    # セッションステートの初期化
    if 'start_time' not in st.session_state:
        st.session_state.start_time = None
    if 'score' not in st.session_state:
        st.session_state.score = 0
    if 'current_question' not in st.session_state:
        st.session_state.current_question = ""
    if 'a' not in st.session_state:
        st.session_state.a = None
    if 'b' not in st.session_state:
        st.session_state.b = None
    if 'game_active' not in st.session_state:
        st.session_state.game_active = False
    if 'user_answer' not in st.session_state:
        st.session_state.user_answer = ""

    # ゲームスタート
    if not st.session_state.game_active:
        if st.button("ゲームスタート"):
            st.session_state.start_time = time.time()
            st.session_state.score = 0
            st.session_state.a, st.session_state.b, st.session_state.current_question = new_question()
            st.session_state.game_active = True

    # ゲーム進行中
    if st.session_state.game_active:
        elapsed_time = time.time() - st.session_state.start_time

        if elapsed_time < game_duration:
            st.write(st.session_state.current_question)
            
            # ユーザーの入力
            user_answer = st.text_input("答えを入力:", key="user_answer")
            
            # ボタンが押されたときの処理
            if st.button("答えをチェック"):
                if user_answer.isdigit() and int(user_answer) == st.session_state.a * st.session_state.b:
                    st.session_state.score += 1
                    st.success("正解！")
                else:
                    st.error("不正解！")

                # 次の問題に進む
                st.session_state.a, st.session_state.b, st.session_state.current_question = new_question()
                st.session_state.user_answer = ""  # 入力欄をリセット
            
            # 現在のスコアと残り時間の表示
            st.write(f"現在のスコア: {st.session_state.score}")
            st.write(f"残り時間: {max(0, game_duration - int(elapsed_time))}秒")
        
        else:
            # ゲーム終了
            st.write(f"ゲーム終了！スコア: {st.session_state.score}")
            if st.button("再スタート"):
                # ゲームの状態をリセット
                st.session_state.game_active = False
                st.session_state.user_answer = ""  # 入力欄をリセット

if __name__ == "__main__":
    main()
