import streamlit as st
from PIL import Image


st.title("Image to Grayscale Converter.")

st.info("Creator: Aryan Kumar Upadhyay")

uploaded_image = st.file_uploader("Upload Image")

with st.expander("Click image on the spot!"):
    # Starting camera by creating instance of camera input
    camera_image = st.camera_input("Camera")

if uploaded_image:
    img = Image.open(uploaded_image)
    gray_img = img.convert("L")
    st.image(gray_img)

if camera_image:
    # Creating instance of the Image
    img = Image.open(camera_image)

    # Converting image into grayscale
    gray_img = img.convert("L")

    # Rendering the image
    st.image(gray_img)