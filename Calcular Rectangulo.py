# Ejercicio: Calcular área y perímetro de un rectángulo a partir de su base y altura
baseRectangulo = float(input("Ingrese la base del rectángulo: "))
alturaRectangulo = float(input("Ingrese la altura del rectángulo: "))

# Fórmulas matemáticas
area = baseRectangulo * alturaRectangulo
perimetro = 2 * (baseRectangulo + alturaRectangulo)

# Mostrar los resultados en pantalla
print("----------------------------------------")
print("El área del rectángulo es: ", area)
print("El perímetro del rectángulo es: ", perimetro)
print("----------------------------------------")