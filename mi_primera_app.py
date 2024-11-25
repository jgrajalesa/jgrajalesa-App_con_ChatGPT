import streamlit as st

# Título de la app
st.title('Mi primera app')

# Autor de la app
st.write('Esta app fue elaborada por Juan Grajales')

# Pregunta al usuario
nombre_usuario = st.text_input('¿Cuál es tu nombre?')

# Mostrar el mensaje de bienvenida
if nombre_usuario:
    st.write(f'{nombre_usuario}, te doy la bienvenida a mi primera app.')
