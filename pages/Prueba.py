import streamlit as st

# Título de la aplicación
st.title("MODELO LSTM CLASIFICADOR")
# Descripción del modelo LSTM
st.markdown("""
            Un modelo LSTM (Long Short-Term Memory) es un tipo de 
            red neuronal recurrente (RNN) especializada en trabajar 
            con datos secuenciales, como series de tiempo, texto y 
            datos de secuencia en general. A diferencia de las RNN 
            tradicionales, que pueden sufrir de desvanecimiento o 
            explosión del gradiente en entrenamientos a largo plazo, 
            las capas LSTM están diseñadas para abordar estos problemas 
            y capturar dependencias a largo plazo en los datos de entrada.
            """)
# Apartado para enviar un dato
dato = st.text_input("Ingrese un dato:")
enviar = st.button("Enviar")

# Verificar si se ha enviado el dato
if enviar:
    st.write("Dato enviado:", dato)