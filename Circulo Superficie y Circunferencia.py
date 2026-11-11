import math

# Lectura del radio del círculo
RADIO = float(input("Ingrese el radio del círculo: "))

# Cálculos de superficie y circunferencia
SUPERFICIE = math.pi * (RADIO ** 2)
PERIMETRO = 2 * math.pi * RADIO

# Resultados
print("La superficie es: ", SUPERFICIE)
print("La circunferencia es: ", PERIMETRO)