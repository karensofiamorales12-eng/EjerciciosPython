# Ejercicio: Determinar si un número real (x) se encuentra en el rango (3.5, 7.8]
x = float(input("Ingrese un número real (x): "))

# Evaluación del rango:
# - Abierto en 3.5 -> estrictamente mayor que 3.5 (x > 3.5)
# - Cerrado en 7.8 -> menor o igual que 7.8 (x <= 7.8)
if x > 3.5 and x <= 7.8:
    print("----------------------------------------")
    print("El número", x, "SÍ se encuentra dentro del rango (3.5, 7.8].")
    print("----------------------------------------")
else:
    print("----------------------------------------")
    print("El número", x, "NO se encuentra dentro del rango (3.5, 7.8].")
    print("----------------------------------------")