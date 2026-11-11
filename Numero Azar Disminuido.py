import random

# Ejercicio: Generar número aleatorio del 10 al 50 y disminuirlo en un 15%

# Generar un número aleatorio entero entre 10 y 50 (inclusive)
numeroAleatorio = random.randint(10, 50)

# Calcular el número disminuido en un 15% (equivalente a multiplicar por 0.85)
numeroDisminuido = numeroAleatorio * 0.85

# Mostrar los resultados en pantalla
print("----------------------------------------")
print("El número aleatorio generado es: ", numeroAleatorio)
print("El número disminuido en un 15% es: ", numeroDisminuido)
print("----------------------------------------")