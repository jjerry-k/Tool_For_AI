import streamlit as st
st.set_page_config(layout="wide") # streamlit import 이후 가장 먼저 설정 해야함, 이후 재선언 시 오류 발생

from auth import is_authenticated, is_logout
import os, threading
from utils.crawler import crawling
from utils.mongo import insert_data, delete_data, update_data, get_data_list
from utils.common import image_viewer, StorageConfig

if is_authenticated():
    
    st.sidebar.text(f"User Name: {st.session_state['username']}")
    is_logout()

    st.sidebar.radio("Task List", options=["Crawling", "Cleaning"], key="task")
    
    st.title("Data Acquistion Page")

    if st.session_state.task == "Crawling": 
        keyword = st.text_input("Keyword")
        flag = st.button("Start crawling")
        if flag:
            crawling_thread = threading.Thread(target=crawling, name="Crawling", args=[st.session_state.username, StorageConfig.JOBS_ROOT, keyword, insert_data])
            crawling_thread.start()
            st.info("Start crawling!")
        
    elif st.session_state.task == "Cleaning": 
        st.session_state.fileindex = 0
        keyword_list = get_data_list(st.session_state["username"])
        st.session_state.keyword = st.sidebar.selectbox("Class", options=[f"{i}: {keyword['keyword']}" for i, keyword in enumerate(keyword_list)])
        num, st.session_state.keyword = st.session_state.keyword.split(": ")
        st.session_state.curr_keyword = keyword_list[int(num)]
        
        image_viewer()