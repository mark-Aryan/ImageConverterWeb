import streamlit as st
from PIL import Image

st.info("Creator: Aryan Kumar Upadhyay")

with st.expander("Start Camera"):
    # Starting camera by creating instance of camera input
    camera_image = st.camera_input("Camera")

if camera_image:
    # Creating instance of the Image
    img = Image.open(camera_image)

    # Converting image into grayscale
    gray_img = img.convert("L")

    # Rendering the image
    st.image(gray_img)
