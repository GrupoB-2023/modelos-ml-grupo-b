import streamlit as st

# Título de la aplicación
st.title("MODELO LSTM")
# Descripción del modelo LSTM
st.markdown("""
            Un modelo LSTM (Long Short-Term Memory) es un tipo de 
            red neuronal recurrente (RNN) especializada en trabajar 
            con datos secuenciales, como series de tiempo, texto y 
            datos de secuencia en general. 
            A diferencia de las RNN tradicionales, que pueden sufrir de desvanecimiento o 
            explosión del gradiente en entrenamientos a largo plazo, 
            las capas LSTM están diseñadas para abordar estos problemas 
            y capturar dependencias a largo plazo en los datos de entrada.
            Para este trabajo
            """)

# Apartado para enviar un dato
start_date = '2018-01-01'  # Se establece la fecha de inicio para los datos de precios
end_date = '2022-12-31'  # Se establece la fecha de fin para los datos de precios
Finit = st.date_input("Ingrese una Fecha de Inicio:")
Fend = st.date_input("Ingrese una Fecha de Final:")
enviar = st.button("Enviar")

# Verificar si se ha enviado el dato
if enviar:
    if Finit and Fend:
        st.write("¡Confirmación enviada!")
    else:
        st.write("Por favor, ingrese una fecha en ambos campos.")

#Codigo Parte 1
