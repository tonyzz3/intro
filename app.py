import streamlit as st 
from PIL import Image

st.title("Mi primera App!")

st.header("No me gusta programar uwu")
st.write("si te copio por que no leo :(")
image = Image.open('stick.jpg')

st.image(image, caption= 'sisoy')
