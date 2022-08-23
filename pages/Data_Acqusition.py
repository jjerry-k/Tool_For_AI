import os
import math
import pandas as pd
from PIL import Image
import streamlit as st
import streamlit.components.v1 as components
st.set_page_config(layout="wide") # streamlit import 이후 가장 먼저 설정 해야함, 이후 재선언 시 오류 발생

from icrawler.builtin import GoogleImageCrawler

from auth import is_authenticated


if is_authenticated():
    st.title("Data Acquistion Page")