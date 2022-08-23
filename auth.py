import streamlit as st

from utils import *
# from streamlit_utils.utils import key_shortcut

def registration(username, password):
    pass    

# 계정 정보 일치여부 확인
def is_valid(username, password):
    user = DB[MONGODB_USER_TABLE].find_one({"name": username})
    if user and verify_password(str(password), user["password"]):
        st.session_state["admin"] = user["admin"]
        st.session_state["password"] = ""
        return True
    else:
        return False

def authenticate():
    # 로그인 기능
    st.session_state.authenticated = False
    cols = st.columns(4)
    cols[1].title("Login")
    st.session_state.username = cols[2].text_input('Username', key='user', value="")
    st.session_state.password = cols[2].text_input('Password', type="password", value="")
    cols[2].button("Login", key='login', on_click=auth_callback)

    # Enter 입력 시 로그인 버튼 눌러지도록 javascript 추가
    # key_shortcut('Login', 13)

def auth_callback():
    st.session_state.authenticated = is_valid(st.session_state.username, st.session_state.password)
    if st.session_state.username and st.session_state.password and not st.session_state.authenticated:
        st.error("아이디나 비밀번호를 확인해주세요.")

def is_authenticated():
    if 'authenticated' not in st.session_state:
        authenticate()
    elif not st.session_state.authenticated:
        authenticate()

    return st.session_state.authenticated