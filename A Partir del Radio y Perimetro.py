import math

# Ejemplo 2.2: A partir del radio, calcular área y perímetro del círculo.
radio = float(input("Ingrese el valor del radio del círculo: "))

# Fórmulas matemáticas
area = math.pi * (radio ** 2)
perimetro = 2 * math.pi * radio

# Mostrar resultados
print("El área del círculo es: ", area)
print("El perímetro del círculo es: ", perimetro)