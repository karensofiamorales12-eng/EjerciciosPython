import math

# Ejercicio: Calcular el volumen de un cilindro a partir de su radio y altura
radio = float(input("Ingrese el radio del cilindro: "))
altura = float(input("Ingrese la altura del cilindro: "))

# Aplicando la fórmula del volumen
volumen = math.pi * (radio ** 2) * altura

# Mostrar el resultado en pantalla
print("----------------------------------------")
print("El volumen del cilindro es: ", volumen)
print("----------------------------------------")