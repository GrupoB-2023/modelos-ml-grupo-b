import streamlit as st

st.set_page_config(
    page_title="Tarea Semana 15",
    page_icon="ðŸ‘‹",
)

st.write("# Despliegue web de modelos del Grupo B 2023-1")

st.sidebar.success("Seleccione un modelo del menu")

st.markdown(
    """
    # Grupo B - Integrantes:
    | Nombre |
    |--|--|
    | Jimenez Casta?eda, Luis Francisco - 15200213  |
    | Del Aguila Febres Brayan - 17200270  |
    | Cordova Sandoval Rafael - 17200268 |
    | Caceres Esta?a Juan Alfonso - 19200288   |
    | Ambrocio Milla Katherine Celine - 18200324  |
    | Rios Sanchez Anthony Ulises - 19200099  |
    | Hidalgo D¨ªaz Sebastian Eduardo - 18200082  |

    ### Especificaciones:
    **Donde muestra las predicciones/los resultados:**
    - Graficamente. 
    - Numericamente los valores de las predicciones (print de dataframe con la prediccion o clasificacion).
    
    **Donde se muestra el EDA:**
    - Ploteo de los precios reales.
    (Ploteo de media movil los precios reales.)

    **Donde el usuario pueda indicar:**
    - El modelo ejecutar.
    - La accion o instrumento financiero que quiera analizar.
"""
)
