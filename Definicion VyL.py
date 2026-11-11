# Definición de variables y lectura de datos
valorIntereses = float(input("Ingresa el valor del interés: "))
periodo = float(input("Ingresa el tiempo: "))
cantidad = float(input("Ingresa cantidad de dinero: "))

# Operaciones
impuestos = valorIntereses * 0.07
totalPagar = cantidad + valorIntereses - impuestos

# Resultado
print("El valor de tu ganancia es:", totalPagar)
