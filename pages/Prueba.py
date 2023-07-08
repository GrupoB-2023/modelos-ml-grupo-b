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
            """)
# Apartado para enviar un dato
Finit = st.text_input("Ingrese una Fecha de Incio:")
Fend = st.text_input("Ingrese una Fecha de Final:")
enviar = st.button("Enviar")

# Verificar si se ha enviado el dato
if enviar:
    st.write("Dato enviado:", dato)
#Codigo Parte 1
import matplotlib.pyplot as plt  # Importación de la biblioteca matplotlib.pyplot para graficar datos
import pandas as pd  # Importación de la biblioteca pandas para manipulación de datos en forma de DataFrame
import numpy as np  # Importación de la biblioteca numpy para operaciones numéricas
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from tensorflow.keras.optimizers import Adam
import yfinance as yf