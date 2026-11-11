# Ejercicio: Leer tres números enteros, multiplicar los dos primeros y dividir por el tercero
num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))
num3 = int(input("Ingrese el tercer número entero (diferente de cero): "))

# Realizamos la multiplicación y luego la división
resultado = (num1 * num2) / num3

# Mostramos el resultado en pantalla
print("El resultado de (num1 * num2) / num3 es: ", resultado)