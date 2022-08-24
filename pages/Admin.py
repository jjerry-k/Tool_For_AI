import streamlit as st
st.set_page_config(layout="wide") # streamlit import 이후 가장 먼저 설정 해야함, 이후 재선언 시 오류 발생

from auth import is_authenticated
from utils.mongo import insert_user, delete_user, get_user

if is_authenticated():
    st.sidebar.text(f"User Name: {st.session_state['username']}")
    st.sidebar.button("Logout")
    
    if not st.session_state.admin:
        st.error("This is the admin page.")
    
    else:
        st.title("Admin Page")

        st.sidebar.radio("Task List", options=["Uset Management", "Task Tracking"], key="task")

        st.radio("Select task", options=["Register", "Delete"], key='job', horizontal=True)

        # Register user
        if st.session_state.job == "Register": 
            st.subheader("Register User")
            cols = st.columns(1)
            new_user = {
                "name": cols[0].text_input('Username', value=""),
                "admin": cols[0].selectbox("Admin", options=[False, True], ),
                "password": cols[0].text_input('Password', value="")
            }

            def callback(): 
                flag = insert_user(new_user)
                if flag:
                    cols[0].text(f"'{new_user['name']}' already exists!")
                else:
                    cols[0].text(f"'{new_user['name']}' registered!")
            cols[0].button("Register", key='register', on_click=callback)

        # Delete user
        elif st.session_state.job == "Delete": 
            st.subheader("Delete User")
            cols = st.columns(1)
            user_list = get_user()
            selected_user = cols[0].selectbox("Username", options=[f"{i+1}. {user['name']}" for i, user in enumerate(user_list)])
    
            selected_user = user_list[int(selected_user.split(".")[0])-1]

            def callback(): 
                if cols[0].button("2nd Check"):
                    flag = delete_user(selected_user)
            
            cols[0].button("Delete", key='delete', on_click=callback)