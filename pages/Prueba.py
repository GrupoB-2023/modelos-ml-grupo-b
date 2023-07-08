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
Finit = st.date_input("Ingrese una Fecha de Inicio:", value=start_date)
Fend = st.date_input("Ingrese una Fecha de Final:", value= end_date)
enviar = st.button("Enviar")

# Verificar si se ha enviado el dato
if enviar:
    if Finit and Fend:
        st.write("¡Confirmación enviada!")
    else:
        st.write("Por favor, ingrese una fecha en ambos campos.")

#Codigo Parte 1
import matplotlib.pyplot as plt  # Importación de la biblioteca matplotlib.pyplot para graficar datos
import pandas as pd  # Importación de la biblioteca pandas para manipulación de datos en forma de DataFrame
import numpy as np  # Importación de la biblioteca numpy para operaciones numéricas
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from tensorflow.keras.optimizers import Adam
import yfinance as yfgit

# Retrieve the Bitcoin price data from Yahoo Finance
i01_BTC_USD = yf.download('BTC-USD', start=start_date, end=end_date)
# Remove the 'Volume' column
i01_BTC_USD.drop('Volume', axis=1, inplace=True)

# Add 'BTC_' prefix to column names
i01_BTC_USD.columns = ['BTC_' + column for column in i01_BTC_USD.columns]

# Se obtienen los datos de precios de Bitcoin de Yahoo Finance
i01_BTC_USD.sample(2)

i01_BTC_USD.shape

# Retrieve the Bitcoin price data from Yahoo Finance
i02_ETH_USD = yf.download('ETH-USD', start=start_date, end=end_date)
# Remove the 'Volume' column
i02_ETH_USD.drop('Volume', axis=1, inplace=True)

# Add 'BTC_' prefix to column names
i02_ETH_USD.columns = ['ETH_' + column for column in i02_ETH_USD.columns]

# Se obtienen los datos de precios de Bitcoin de Yahoo Finance
i02_ETH_USD.sample(2)

i02_ETH_USD.shape

# Concatenate the DataFrames
df = pd.concat([i02_ETH_USD, i01_BTC_USD], axis=1)

df.sample(2)

# Retrieve the Bitcoin price data from Yahoo Finance
i03_GLD = yf.download('GLD', start=start_date, end=end_date)
# Remove the 'Volume' column
i03_GLD.drop('Volume', axis=1, inplace=True)

# Add 'BTC_' prefix to column names
i03_GLD.columns = ['GLD_' + column for column in i03_GLD.columns]

# Se obtienen los datos de precios de Bitcoin de Yahoo Finance
i03_GLD.sample(2)

i03_GLD.shape

# Concatenate the DataFrames
df02 = pd.concat([i03_GLD , df], axis=1)

df02