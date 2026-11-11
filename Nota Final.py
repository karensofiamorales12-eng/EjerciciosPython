# Ejemplo 2.4: Calcular la nota definitiva a partir del promedio de 4 notas parciales.

# Solicitar las 4 notas al usuario
nota1 = float(input("Ingrese la primera nota parcial: "))
nota2 = float(input("Ingrese la segunda nota parcial: "))
nota3 = float(input("Ingrese la tercera nota parcial: "))
nota4 = float(input("Ingrese la cuarta nota parcial: "))

# Cálculo del promedio (media aritmética)
notaDefinitiva = (nota1 + nota2 + nota3 + nota4) / 4

# Mostrar el resultado final
print("La nota definitiva en la asignatura es: ", notaDefinitiva)