import streamlit as st 
from PIL import Image

st.title("Mi primera App!")

st.header("No me gusta programar uwu")
st.write("si te copio por que no leo :(")
image = Image.open('stick.jpg')

st.image(image, caption= 'sisoy')

texto = st.text_input('we are the world', 'we are the children')
st.write ('we are the one who makes a brighter day', texto)

st.subheader("so let´s start giving")

coll, coll2 = st.colums(2)

with coll: 
  st.subheader ("Martha tiene un marca pasos")
  st.write ("Sufre mamón, devuelveme a mi chica") 
  resp= st. checkbox("Mamma mia, here we go again")
  if resp:
    st.write("AJU NICE!")
