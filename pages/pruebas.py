import streamlit as st

# Título de la aplicación
st.title("Envío de fecha")

# Apartado para enviar una fecha
fecha = st.date_input("Ingrese una fecha:")

# Verificar si se ha enviado la fecha
if fecha is not None:
    st.write("Fecha enviada:", fecha)