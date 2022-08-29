import streamlit as st
st.set_page_config(layout="wide") # streamlit import 이후 가장 먼저 설정 해야함, 이후 재선언 시 오류 발생

from auth import is_authenticated
import os

if is_authenticated():
    
    st.sidebar.text(f"User Name: {st.session_state['username']}")
    st.sidebar.button("Logout")

    st.sidebar.radio("Task List", options=["Crawling", "Cleaning"], key="task")
    
    st.title("Data Acquistion Page")

    if st.session_state.task == "Crawling": 
        keyword = st.text_input("Keyword")
        flag = st.button("Start crawling")
        if flag:
            os.system(f"mkdir -p /disk/test/{keyword}")
            os.system(f"nohup poetry run python utils/crawling.py --root /disk/test --keyword {keyword} > /disk/test/{keyword}/log.out &")

        # 크롤링 완료 여부 & DB 연동

    elif st.session_state.task == "Cleaning": 
        st.session_state["keyword"] = st.text_input("Keyword")