import streamlit as st
import pandas as pd

# Título de la app
st.title("Cálculo del PAPA (Promedio Acumulado Ponderado por Asignatura)")

# Crear una lista vacía para almacenar los datos de las asignaturas
if 'asignaturas' not in st.session_state:
    st.session_state['asignaturas'] = []

# Función para agregar una nueva asignatura
def agregar_asignatura(nombre, calificacion, creditos, tipologia):
    st.session_state['asignaturas'].append({
        "Nombre": nombre,
        "Calificación": calificacion,
        "Créditos": creditos,
        "Tipología": tipologia
    })

# Formulario para ingresar los datos de una asignatura
with st.form(key="asignatura_form"):
    nombre = st.text_input("Nombre de la asignatura")
    calificacion = st.number_input("Calificación obtenida (0-10)", min_value=0.0, max_value=10.0, step=0.1)
    creditos = st.number_input("Créditos de la asignatura", min_value=1, step=1)
    tipologia = st.selectbox("Tipología de la asignatura", ["Teoría", "Práctica", "Optativa"])
    
    submit_button = st.form_submit_button("Agregar Asignatura")
    
    if submit_button:
        # Agregar la asignatura a la lista
        agregar_asignatura(nombre, calificacion, creditos, tipologia)
        st.success("Asignatura agregada correctamente")

# Mostrar las asignaturas ingresadas
if st.session_state['asignaturas']:
    df_asignaturas = pd.DataFrame(st.session_state['asignaturas'])
    st.write("### Asignaturas Registradas")
    st.dataframe(df_asignaturas)

    # Cálculo del PAPA global
    total_creditos = df_asignaturas["Créditos"].sum()
    ponderado_total = sum(df_asignaturas["Calificación"] * df_asignaturas["Créditos"])
    papa_global = ponderado_total / total_creditos if total_creditos > 0 else 0
    st.write(f"### PAPA Global: {papa_global:.2f}")

    # Cálculo del PAPA por tipología de asignatura
    st.write("### PAPA por Tipología de Asignatura")
    tipos = df_asignaturas["Tipología"].unique()
    for tipo in tipos:
        asignaturas_tipo = df_asignaturas[df_asignaturas["Tipología"] == tipo]
        total_creditos_tipo = asignaturas_tipo["Créditos"].sum()
        ponderado_tipo = sum(asignaturas_tipo["Calificación"] * asignaturas_tipo["Créditos"])
        papa_tipo = ponderado_tipo / total_creditos_tipo if total_creditos_tipo > 0 else 0
        st.write(f"{tipo}: {papa_tipo:.2f}")

else:
    st.write("No se han ingresado asignaturas aún.")
