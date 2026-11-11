import math

# Lectura de datos
num = float(input("Ingrese un número: "))

# Cálculos usando la librería math
seno = math.sin(num)
coseno = math.cos(num)
tangente = math.tan(num)
rais = math.sqrt(num)           # Equivale a RC (Raíz Cuadrada)
logaritmoNatural = math.log(num) # Equivale a LN (Logaritmo Natural)

# Resultados
print(f"\nResultados para el número {num}:")
print(f"Seno: {seno}")
print(f"Coseno: {coseno}")
print(f"Tangente: {tangente}")
print(f"Raíz cuadrada: {rais}")
print(f"Logaritmo natural: {logaritmoNatural}")