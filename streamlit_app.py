import numpy as np
import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

st.write("# Predicción de gasto de una actividad")
st.image("c.jpg", caption="Predicción del costo de una actividad.")

st.header("Datos de la actividad")

def user_input_features():
   

    Actividad = st.number_input(
        "Actividad por número (Farmacia y doctor = 1) (Gastos inecesarios = 2) (Cena con amigos = 3) (Cena con la novia = 4) (Gasolina = 5) (Oxxo = 6) (Súper = 7):",
        min_value=1,
        max_value=10,
        value=1,
        step=1,
    )

    Presupuesto = st.number_input(
        "Presupuesto estimado (en pesos):",
        min_value=0.0,
        max_value=10000.0,
        value=0.0,
        step=50.0,
    )

    Tiempo = st.number_input(
        "Tiempo invertido en minutos:",
        min_value=0,
        max_value=300,
        value=0,
        step=5,
    )

    Tipo = st.number_input(
        "Tipo (Alimentos/Salud = 1) (Entretenimiento/Ocio = 2) (Transporte= 3):",
        min_value=1,
        max_value=3,
        value=1,
        step=1,
    )

    Momento = st.number_input(
        "Momento (Mañana = 1) (Tarde = 2) (Noche = 3):",
        min_value=1,
        max_value=3,
        value=1,
        step=1,
    )

    Personas = st.number_input(
        "Número de personas: 1-4",
        min_value=1,
        max_value=10,
        value=1,
        step=1,
    )

    
    user_input_data = {
        "Actividad": Actividad,
        "Presupuesto_num": Presupuesto,
        "Tiempo invertido en minutos": Tiempo,
        "Tipo": Tipo,
        "Momento": Momento,
        "No. de personas": Personas,
    }

    features = pd.DataFrame(user_input_data, index=[0])
    return features


df = user_input_features()



datos = pd.read_csv("ActividadFinal.csv", encoding="latin-1")


X = datos.drop(columns='Costo')
y = datos['Costo']

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=1613726)
LR = LinearRegression()
LR.fit(X_train,y_train)

b1 = LR.coef_
b0 = LR.intercept_
prediccion = b0 + b1[0]*df['Actividad'] + b1[1]*df['Presupuesto_num'] + b1[2]*df['Tiempo invertido en minutos'] + b1[3]*df['Tipo'] + b1[4]*df['Momento'] + b1[5]*df['No. de personas']

st.subheader("Gasto de la actividad")
st.write(f"El gasto final es: **${prediccion:.2f}**")
