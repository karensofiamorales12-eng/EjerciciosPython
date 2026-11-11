import random

# Ejercicio: Generar número aleatorio del 0 al 200 y aumentarlo en un 30%

# Generar un número aleatorio entero entre 0 y 200 (inclusive)
numeroAleatorio = random.randint(0, 200)

# Calcular el número aumentado en un 30% (equivalente a multiplicar por 1.30)
numeroAumentado = numeroAleatorio * 1.30

# Mostrar los resultados en pantalla
print("----------------------------------------")
print("El número aleatorio generado es: ", numeroAleatorio)
print("El número aumentado en un 30% es: ", numeroAumentado)
print("----------------------------------------")