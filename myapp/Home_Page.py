import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import streamlit as st
from PIL import Image
import base64

st.set_page_config(
    page_title="maize crop",
    page_icon=":corn:",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items={
                'Get Help': 'https://www.extremelycoolapp.com/help',
                'Report a bug': "https://www.extremelycoolapp.com/bug",
                'About': "# This is a header. This is an *extremely* cool app!"
            }
)
#st.logo(image="/assets/logo.png",size="large")

# def get_base64(file_path):
#     with open(file_path, "rb") as f:
#         data = f.read()
#     return base64.b64encode(data).decode()

# bg_img = get_base64("assets/maize-leaf.png")

# st.markdown(
#     f"""
#     <style>
#     .stApp {{
#         background-image: url("data:image/png;base64,{bg_img}");
#         background-size: cover;
#         background-position: center;
#         background-repeat: no-repeat;
#         background-attachment: fixed;
#     }}
#     </style>
#     """,
#     unsafe_allow_html=True
# )



st.title("Welcome to the Maize Crop Dashboard 🌽")
# Add custom CSS for columns
st.markdown("""
<style>
    /* Target the first column */
    div[data-testid="column"]:nth-child(1) {
        background-color: #e8f4f8;
    }
    
    /* Target the second column */
    div[data-testid="column"]:nth-child(2) {
        background-color: #ff0000;
    }
</style>
""", unsafe_allow_html=True)

# Create columns
col1, col2 = st.columns(2,border=True,vertical_alignment="bottom")

with col1:
    st.write("This is column 1 with custom styling")
    
with col2:
    st.write("This is column 2 with custom styling")
