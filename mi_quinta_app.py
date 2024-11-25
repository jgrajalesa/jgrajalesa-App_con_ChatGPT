import streamlit as st
import random

# Título de la app
st.title("Ruleta Aleatoria")

# Descripción de la app
st.write("Esta es una ruleta aleatoria. Ingresa algunas opciones y haz girar la ruleta para seleccionar una aleatoriamente.")

# Ingreso de opciones
opciones = st.text_area("Ingresa tus opciones separadas por comas (Ejemplo: Rojo, Azul, Verde, Amarillo)", "")

# Convertir las opciones ingresadas en una lista
if opciones:
    lista_opciones = [opcion.strip() for opcion in opciones.split(",")]

    # Botón para girar la ruleta
    if st.button("Girar la ruleta"):
        if len(lista_opciones) > 0:
            seleccion = random.choice(lista_opciones)
            st.write(f"🎉 ¡La opción seleccionada es: **{seleccion}**! 🎉")
        else:
            st.write("Por favor, ingresa algunas opciones válidas.")
else:
    st.write("Por favor, ingresa las opciones que deseas en la ruleta.")

