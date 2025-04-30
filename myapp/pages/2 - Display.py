#Import basic libraries
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
#import streamlit library
import streamlit as st
from PIL import Image

# Custom CSS to add a nice border
# st.markdown(
#     """
#     <style>
#     .card {
#         background-color: #f9f9f9;
#         padding: 2rem;
#         border-radius: 10px;
#         box-shadow: 0 4px 8px rgba(0,0,0,0.1);
#         margin: 2rem 0;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )
st.title("Display Us Page")
st.markdown("---")

col1, col2, col3 = st.columns(3,gap="medium",border=True,vertical_alignment="bottom")
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

st.markdown("---")
# Use camera to take picture
col2, col3 = st.columns(2)  # Center column is larger

with col2:
    image_data = st.camera_input("Take a photo of the maize leaf")


# colimage1,colimage2 = st.columns(2)
with col3:
    if image_data is not None:
        st.markdown("""    """)
        image = Image.open(image_data)
        st.image(image, caption="Captured Maize Leaf", width=800)
        image.save("captured_maize_leaf.jpg")
        st.success("Image saved successfully!")

# Layout: 3 columns to center the content
# col1, col2, col3 = st.columns([1, 2, 1])
# with col2:
#     # Button to activate camera
#     if st.button("📸 Open Camera to Capture Maize Leaf"):
#         # Camera input (shows only after button click)
#         image_data = st.camera_input("Capture Maize Leaf Image")

#         if image_data is not None:
#             image = Image.open(image_data)
#             st.image(image, caption="Captured Maize Leaf", use_container_width=True)
#             image.save("captured_maize_leaf.jpg")
#             st.success("Image saved successfully!")

# st.markdown(
#     """
#     <style>
#     [data-testid="stCameraInput"] video {
#         width: 400px !important;
#         height: auto !important;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )