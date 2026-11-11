# Ejercicio: Ingresar dos palabras (A y B), intercambiar sus valores y mostrarlas
A = input("Ingrese el valor para la palabra A: ")
B = input("Ingrese el valor para la palabra B: ")

# Proceso de intercambio utilizando una variable auxiliar
aux = A
A = B
B = aux

# Mostrar los resultados después del intercambio
print("----------------------------------------")
print("¡Intercambio realizado con éxito!")
print("El nuevo contenido de A es: ", A)
print("El nuevo contenido de B es: ", B)
print("----------------------------------------")