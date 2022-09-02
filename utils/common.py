import os
import cv2
import hashlib

import numpy as np
import streamlit as st

from PIL import Image

from config import StorageConfig

IMG_FORMAT = ["jpg", "jpeg", "tiff", "tif", "png", "bmp"]

def check_img_format(filename):
    return filename.split(".")[-1].lower() in IMG_FORMAT

def load_img(path):
    try:
        try:
            img = Image.open(path).convert("RGB").resize((700, 700))
        except:
            img = cv2.imread(path)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img = cv2.resize(img, (700, 700))
        return np.array(img)
    except:
        print("Can't Read")

def get_file_hash(filepath):
    with open(filepath, 'rb') as f:
        md5 = hashlib.md5()
        md5.update(f.read())
    return md5.hexdigest()

def image_viewer():
    cols = st.columns([1, 1])
    
    image_file_path = os.path.join(
                                StorageConfig.JOBS_ROOT,
                                st.session_state.username,
                                st.session_state.keyword, 
                                st.session_state.curr_keyword["data"][st.session_state.fileindex]["filename"]
                                )
    
    img = load_img(image_file_path)
    cols[0].image(img, caption=image_file_path.split("/")[-1])
    