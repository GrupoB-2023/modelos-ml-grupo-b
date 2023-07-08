import streamlit as st

# Título de la aplicación
st.title("Envío de datos")

# Apartado para enviar un dato
dato = st.text_input("Ingrese un dato:")
enviar = st.button("Enviar")

# Verificar si se ha enviado el dato
if enviar:
    st.write("Dato enviado:", dato)