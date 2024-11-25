import streamlit as st
import pandas as pd
import datetime

# Título de la app
st.title("Registro de Finanzas Personales")

# Función para calcular las diferencias entre lo presupuestado y lo real
def calcular_diferencia(presupuestado, real):
    return real - presupuestado

# Crear una base de datos de ejemplo (en una implementación real, esta podría ser una base de datos)
if 'registro' not in st.session_state:
    st.session_state['registro'] = pd.DataFrame(columns=["Fecha", "Categoría", "Presupuesto", "Real", "Tipo"])

# Formulario para ingresar presupuesto y gastos
with st.form(key="finanzas_form"):
    fecha = st.date_input("Fecha", value=datetime.date.today())
    categoria = st.selectbox("Categoría", ["Ingreso", "Gasto", "Meta de Ahorro"])
    presupuesto = st.number_input("Presupuesto", min_value=0.0, step=0.01)
    real = st.number_input("Real", min_value=0.0, step=0.01)
    tipo = st.selectbox("Tipo de transacción", ["Ingreso", "Gasto", "Meta de Ahorro"])
    
    submit_button = st.form_submit_button("Registrar")
    
    # Al presionar el botón de registrar, se añade al registro
    if submit_button:
        # Agregar los datos a la sesión de registro
        st.session_state['registro'] = st.session_state['registro'].append({
            "Fecha": fecha,
            "Categoría": categoria,
            "Presupuesto": presupuesto,
            "Real": real,
            "Tipo": tipo
        }, ignore_index=True)
        st.success("Registro agregado exitosamente.")

# Mostrar el registro de finanzas
st.write("### Registro de Finanzas")
st.dataframe(st.session_state['registro'])

# Reporte de diferencias
st.write("### Reporte de Diferencias")
# Filtrar por semana y mes
fecha_inicio_semana = datetime.date.today() - datetime.timedelta(days=datetime.date.today().weekday())  # inicio de la semana
fecha_inicio_mes = datetime.date.today().replace(day=1)  # inicio del mes

# Filtrar el registro por semana y mes
registro_semana = st.session_state['registro'][st.session_state['registro']['Fecha'] >= fecha_inicio_semana]
registro_mes = st.session_state['registro'][st.session_state['registro']['Fecha'] >= fecha_inicio_mes]

# Calcular las diferencias para la semana y el mes
diferencia_semana = registro_semana['Real'] - registro_semana['Presupuesto']
diferencia_mes = registro_mes['Real'] - registro_mes['Presupuesto']

# Mostrar los reportes
st.write(f"**Diferencias de la Semana (del {fecha_inicio_semana} en adelante):**")
st.write(f"Diferencia Total de la Semana: {diferencia_semana.sum():.2f}")
st.write(f"**Diferencias del Mes (del {fecha_inicio_mes} en adelante):**")
st.write(f"Diferencia Total del Mes: {diferencia_mes.sum():.2f}")

# Mostrar un resumen de metas de ahorro (si existe alguna meta)
st.write("### Resumen de Metas de Ahorro")
metas_ahorro = st.session_state['registro'][st.session_state['registro']['Tipo'] == "Meta de Ahorro"]
if not metas_ahorro.empty:
    st.dataframe(metas_ahorro)
else:
    st.write("No tienes metas de ahorro registradas.")
