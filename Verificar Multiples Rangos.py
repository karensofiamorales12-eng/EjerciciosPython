# Evaluación de múltiples rangos para un número real (x)
x = float(input("Ingrese un número real (x): "))

# Evaluación de los rangos según el árbol de decisión
if (x > 3.5 and x <= 7.8) or (x >= 9.3 and x < 4.5) or (x >= 23.4 and x <= 45.3):
    print("----------------------------------------")
    print("¡Está en el rango!")
    print("----------------------------------------")
else:
    print("----------------------------------------")
    print("No está en el rango.")
    print("----------------------------------------")