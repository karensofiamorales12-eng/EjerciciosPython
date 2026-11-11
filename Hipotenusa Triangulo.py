import math

# Ejercicio: Calcular la hipotenusa de un triángulo rectángulo usando el teorema de Pitágoras
cateto1 = float(input("Ingrese el valor del primer cateto: "))
cateto2 = float(input("Ingrese el valor del segundo cateto: "))

# Aplicando el teorema de Pitágoras con la función raíz cuadrada (sqrt) y potencia (**)
hipotenusa = math.sqrt((cateto1 ** 2) + (cateto2 ** 2))

# Mostrar el resultado en pantalla
print("----------------------------------------")
print("La hipotenusa del triángulo rectángulo es: ", hipotenusa)
print("----------------------------------------")