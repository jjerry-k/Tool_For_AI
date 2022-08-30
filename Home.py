import streamlit as st
st.set_page_config(layout="wide") # streamlit import 이후 가장 먼저 설정 해야함, 이후 재선언 시 오류 발생

from PIL import Image

st.write("# This is Application for AI")

# st.image(Image.open('./figure/Tom&Jerry.jpeg'))

st.markdown(
    """
    ### Features
    - Admin
        - User management
        - Job inspection    
        - Data crawling
        - Data cleaning
    - User
        - Data crawling
        - Data cleaning

"""
)