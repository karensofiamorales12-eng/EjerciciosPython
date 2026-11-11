import math

# Ejemplo 2.3: Uso de las principales funciones matemáticas con un número ingresado
num = float(input("Ingrese un número real: "))

print("----------------------------------------")
print("Resultados de las funciones para: ", num)
print("Valor absoluto: ", abs(num))
print("Raíz cuadrada: ", math.sqrt(num))
print("Parte entera (Truncado): ", math.trunc(num))
print("Redondeo: ", round(num))
print("Seno: ", math.sin(num))
print("Coseno: ", math.cos(num))
print("----------------------------------------")