# Ejercicio: Generación de números impares modificando el límite dinámicamente
n = float(input("Ingresa la cantidad de números: "))
num = 1

while num <= n:
    n = n + 1
    print(num)
    num = num + 2