import streamlit as st

# Función para realizar conversiones
def convertir(valor, tipo_conversion):
    if tipo_conversion == "Celsius a Fahrenheit":
        return (valor * 9/5) + 32
    elif tipo_conversion == "Fahrenheit a Celsius":
        return (valor - 32) * 5/9
    elif tipo_conversion == "Celsius a Kelvin":
        return valor + 273.15
    elif tipo_conversion == "Kelvin a Celsius":
        return valor - 273.15
    elif tipo_conversion == "Pies a metros":
        return valor * 0.3048
    elif tipo_conversion == "Metros a pies":
        return valor / 0.3048
    elif tipo_conversion == "Pulgadas a centímetros":
        return valor * 2.54
    elif tipo_conversion == "Centímetros a pulgadas":
        return valor / 2.54
    elif tipo_conversion == "Libras a kilogramos":
        return valor * 0.453592
    elif tipo_conversion == "Kilogramos a libras":
        return valor / 0.453592
    elif tipo_conversion == "Onzas a gramos":
        return valor * 28.3495
    elif tipo_conversion == "Gramos a onzas":
        return valor / 28.3495
    elif tipo_conversion == "Galones a litros":
        return valor * 3.78541
    elif tipo_conversion == "Litros a galones":
        return valor / 3.78541
    elif tipo_conversion == "Pulgadas cúbicas a centímetros cúbicos":
        return valor * 16.387
    elif tipo_conversion == "Centímetros cúbicos a pulgadas cúbicas":
        return valor / 16.387
    elif tipo_conversion == "Horas a minutos":
        return valor * 60
    elif tipo_conversion == "Minutos a segundos":
        return valor * 60
    elif tipo_conversion == "Días a horas":
        return valor * 24
    elif tipo_conversion == "Semanas a días":
        return valor * 7
    elif tipo_conversion == "Millas por hora a kilómetros por hora":
        return valor * 1.60934
    elif tipo_conversion == "Kilómetros por hora a metros por segundo":
        return valor / 3.6
    elif tipo_conversion == "Nudos a millas por hora":
        return valor * 1.15078
    elif tipo_conversion == "Metros por segundo a pies por segundo":
        return valor * 3.28084
    elif tipo_conversion == "Metros cuadrados a pies cuadrados":
        return valor * 10.7639
    elif tipo_conversion == "Pies cuadrados a metros cuadrados":
        return valor / 10.7639
    elif tipo_conversion == "Kilómetros cuadrados a millas cuadradas":
        return valor * 0.386102
    elif tipo_conversion == "Millas cuadradas a kilómetros cuadrados":
        return valor / 0.386102
    elif tipo_conversion == "Julios a calorías":
        return valor * 0.239006
    elif tipo_conversion == "Calorías a kilojulios":
        return valor * 0.004184
    elif tipo_conversion == "Kilovatios-hora a megajulios":
        return valor * 3.6
    elif tipo_conversion == "Megajulios a kilovatios-hora":
        return valor / 3.6
    elif tipo_conversion == "Pascales a atmósferas":
        return valor / 101325
    elif tipo_conversion == "Atmósferas a pascales":
        return valor * 101325
    elif tipo_conversion == "Barras a libras por pulgada cuadrada":
        return valor * 14.5038
    elif tipo_conversion == "Libras por pulgada cuadrada a bares":
        return valor / 14.5038
    elif tipo_conversion == "Megabytes a gigabytes":
        return valor / 1024
    elif tipo_conversion == "Gigabytes a Terabytes":
        return valor / 1024
    elif tipo_conversion == "Kilobytes a megabytes":
        return valor / 1024
    elif tipo_conversion == "Terabytes a petabytes":
        return valor / 1024
    else:
        return "Conversión no disponible"

# Título de la app
st.title("Conversor Universal")

# Categoría de la conversión
categoria = st.selectbox("Selecciona una categoría de conversión:",
                         ("Temperatura", "Longitud", "Peso/Masa", "Volumen", "Tiempo", 
                          "Velocidad", "Área", "Energía", "Presión", "Tamaño de datos"))

# Tipos de conversión según la categoría seleccionada
if categoria == "Temperatura":
    tipo_conversion = st.selectbox("Selecciona el tipo de conversión:",
                                   ("Celsius a Fahrenheit", "Fahrenheit a Celsius", "Celsius a Kelvin", "Kelvin a Celsius"))
elif categoria == "Longitud":
    tipo_conversion = st.selectbox("Selecciona el tipo de conversión:",
                                   ("Pies a metros", "Metros a pies", "Pulgadas a centímetros", "Centímetros a pulgadas"))
elif categoria == "Peso/Masa":
    tipo_conversion = st.selectbox("Selecciona el tipo de conversión:",
                                   ("Libras a kilogramos", "Kilogramos a libras", "Onzas a gramos", "Gramos a onzas"))
elif categoria == "Volumen":
    tipo_conversion = st.selectbox("Selecciona el tipo de conversión:",
                                   ("Galones a litros", "Litros a galones", "Pulgadas cúbicas a centímetros cúbicos", 
                                    "Centímetros cúbicos a pulgadas cúbicas"))
elif categoria == "Tiempo":
    tipo_conversion = st.selectbox("Selecciona el tipo de conversión:",
                                   ("Horas a minutos", "Minutos a segundos", "Días a horas", "Semanas a días"))
elif categoria == "Velocidad":
    tipo_conversion = st.selectbox("Selecciona el tipo de conversión:",
                                   ("Millas por hora a kilómetros por hora", "Kilómetros por hora a metros por segundo", 
                                    "Nudos a millas por hora", "Metros por segundo a pies por segundo"))
elif categoria == "Área":
    tipo_conversion = st.selectbox("Selecciona el tipo de conversión:",
                                   ("Metros cuadrados a pies cuadrados", "Pies cuadrados a metros cuadrados", 
                                    "Kilómetros cuadrados a millas cuadradas", "Millas cuadradas a kilómetros cuadrados"))
elif categoria == "Energía":
    tipo_conversion = st.selectbox("Selecciona el tipo de conversión:",
                                   ("Julios a calorías", "Calorías a kilojulios", "Kilovatios-hora a megajulios", 
                                    "Megajulios a kilovatios-hora"))
elif categoria == "Presión":
    tipo_conversion = st.selectbox("Selecciona el tipo de conversión:",
                                   ("Pascales a atmósferas", "Atmósferas a pascales", "Barras a libras por pulgada cuadrada", 
                                    "Libras por pulgada cuadrada a bares"))
elif categoria == "Tamaño de datos":
    tipo_conversion = st.selectbox("Selecciona el tipo de conversión:",
                                   ("Megabytes a gigabytes", "Gigabytes a Terabytes", "Kilobytes a megabytes", 
                                    "Terabytes a petabytes"))

# Entrada del valor a convertir
valor = st.number_input("Introduce el valor que deseas convertir:", min_value=0.0)

# Mostrar el resultado si se ha introducido un valor
if valor:
    resultado = convertir(valor, tipo_conversion)
    st.write(f"El resultado de la conversión es: {resultado}")
  
