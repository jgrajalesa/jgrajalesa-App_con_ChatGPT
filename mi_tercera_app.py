import streamlit as st
import pandas as pd
import datetime as dt

# Inicializar datos
if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=["Fecha", "Categoría", "Monto", "Tipo", "Descripción"])

# Función para agregar registros
def agregar_registro(fecha, categoria, monto, tipo, descripcion):
    nuevo_registro = {"Fecha": fecha, "Categoría": categoria, "Monto": monto, "Tipo": tipo, "Descripción": descripcion}
    st.session_state.data = pd.concat([st.session_state.data, pd.DataFrame([nuevo_registro])], ignore_index=True)

# Título de la app
st.title("💰 Registro de Finanzas Personales")

# Sección para agregar registros
st.header("Agregar Registro")
with st.form("registro_form"):
    fecha = st.date_input("Fecha", dt.date.today())
    categoria = st.selectbox("Categoría", ["Alimentos", "Transporte", "Entretenimiento", "Ahorro", "Otros"])
    monto = st.number_input("Monto", min_value=0.0, step=0.01)
    tipo = st.radio("Tipo", ["Ingreso", "Gasto"])
    descripcion = st.text_area("Descripción")
    enviado = st.form_submit_button("Agregar")
    if enviado:
        agregar_registro(fecha, categoria, monto, tipo, descripcion)
        st.success("Registro agregado correctamente.")

# Mostrar registros
st.header("Registros actuales")
if not st.session_state.data.empty:
    st.dataframe(st.session_state.data)
else:
    st.write("No hay registros aún.")

# Generar reportes
st.header("📊 Reportes")
tipo_reporte = st.selectbox("Selecciona el tipo de reporte", ["Semanal", "Mensual"])

if not st.session_state.data.empty:
    hoy = dt.date.today()
    if tipo_reporte == "Semanal":
        inicio_semana = hoy - dt.timedelta(days=hoy.weekday())
        fin_semana = inicio_semana + dt.timedelta(days=6)
        reporte = st.session_state.data[
            (st.session_state.data["Fecha"] >= inicio_semana) & (st.session_state.data["Fecha"] <= fin_semana)
        ]
        st.subheader(f"Reporte semanal ({inicio_semana} - {fin_semana})")
    elif tipo_reporte == "Mensual":
        inicio_mes = hoy.replace(day=1)
        fin_mes = (inicio_mes + pd.DateOffset(months=1) - pd.DateOffset(days=1)).date()
        reporte = st.session_state.data[
            (st.session_state.data["Fecha"] >= inicio_mes) & (st.session_state.data["Fecha"] <= fin_mes)
        ]
        st.subheader(f"Reporte mensual ({inicio_mes} - {fin_mes})")

    if not reporte.empty:
        ingresos = reporte[reporte["Tipo"] == "Ingreso"]["Monto"].sum()
        gastos = reporte[reporte["Tipo"] == "Gasto"]["Monto"].sum()
        diferencia = ingresos - gastos
        st.write(f"Total de ingresos: ${ingresos:.2f}")
        st.write(f"Total de gastos: ${gastos:.2f}")
        st.write(f"Diferencia: ${diferencia:.2f}")
    else:
        st.write("No hay registros para este período.")
        diferencia = 0  # Asegurarse de que diferencia esté definida aunque no haya registros
else:
    st.write("No hay datos para generar reportes.")
    diferencia = 0

# Sección para metas de ahorro
st.header("🎯 Metas de ahorro")
meta_ahorro = st.number_input("Define tu meta de ahorro mensual ($)", min_value=0.0, step=0.01)
if diferencia >= meta_ahorro:
    st.success(f"¡Felicidades! Has alcanzado tu meta de ahorro. Excedente: ${diferencia - meta_ahorro:.2f}")
else:
    st.warning(f"Te faltan ${meta_ahorro - diferencia:.2f} para alcanzar tu meta.")
