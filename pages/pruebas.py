import streamlit as st
from datetime import datetime

# Título de la aplicación
st.title("Envío de fecha")

# Apartado para enviar una fecha
fecha_str = st.text_input("Ingrese una fecha en formato año-mes-día (YYYY-MM-DD):")

# Verificar si se ha enviado la fecha
if fecha_str:
    try:
        fecha = datetime.strptime(fecha_str, "%Y-%m-%d").date()
        st.write("Fecha enviada:", fecha)
    except ValueError:
        st.write("Formato de fecha incorrecto. Asegúrese de ingresar en el formato correcto (YYYY-MM-DD).")