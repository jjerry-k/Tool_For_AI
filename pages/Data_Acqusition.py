import streamlit as st
st.set_page_config(layout="wide") # streamlit import 이후 가장 먼저 설정 해야함, 이후 재선언 시 오류 발생

from auth import is_authenticated, is_logout
import os, threading
from utils.crawler import crawling, crawling_test
from utils.mongo import insert_data, delete_data, update_data

if is_authenticated():
    
    st.sidebar.text(f"User Name: {st.session_state['username']}")
    is_logout()

    st.sidebar.radio("Task List", options=["Crawling", "Cleaning"], key="task")
    
    st.title("Data Acquistion Page")

    if st.session_state.task == "Crawling": 
        keyword = st.text_input("Keyword")
        flag = st.button("Start crawling")
        if flag:
            root = "/disk/jobs/"
            keyword_path = os.path.join(root, keyword)
            # os.system(f"nohup poetry run python utils/crawler.py --user {st.session_state.username} --root {root} --keyword {keyword} 1> /dev/null 2>&1 &")
            # os.system(f"nohup poetry run python utils/crawler.py --user {st.session_state.username} --root {root} --keyword {keyword}")
            crawling_thread = threading.Thread(target=crawling_test, name="Crawling", args=[st.session_state.username, root, keyword, insert_data])
            crawling_thread.start()

            st.info("Start crawling!")
        # 크롤링 완료 여부 & DB 연동

    elif st.session_state.task == "Cleaning": 
        st.session_state["keyword"] = st.text_input("Keyword")