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

col1, col2 = st.columns(2)

with col1: 
  st.subheader ("Martha tiene un marca pasos")
  st.write ("Sufre mamón, devuelveme a mi chica") 
  resp= st. checkbox("Mamma mia, here we go again")
  if resp:
    st.write("AJU NICE!")

with col2:
  stsubheader("mimimimi")
  modo = st.radio("there was something in the air that night, the star we bright...", ( "FRANCISCO", "HERNANDO", "FERNANDO"))
  if modo == "FRANCISCO":
    st.write("vete a ver mamma mia plox")
  if modo == "HERNANDO":
    st.write("pues, puedo entenderlo, but u stupid????")
  if modo == "FERNANDO":
    st.write ("THEY WERE SHINYING THERE FOR U N ME, FOR LIBERTY FERNANDOOOOO")
  
