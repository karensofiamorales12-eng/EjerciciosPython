# Ejemplo 2.5: Cálculo de intereses de un CDT y valor total a retirar con retención en la fuente del 7%.
cantidad = float(input("Ingrese la cantidad de dinero invertida: "))
porcentajeInteres = float(input("Ingrese el porcentaje de interés (ej: ingrese 0.05 si es 5%): "))
periodo = float(input("Ingrese el periodo de tiempo en días: "))

# Cálculo de los intereses ganados según la fórmula del enunciado
valorIntereses = (cantidad * porcentajeInteres * periodo) / 360

# Cálculo del 7% de descuento por retención en la fuente sobre los intereses
retencion = valorIntereses * 0.07

# Cálculo del valor total a retirar (capital inicial + intereses menos la retención)
valorTotalRetirar = cantidad + (valorIntereses - retencion)

# Mostrar resultados detallados
print("----------------------------------------")
print("Intereses brutos ganados: $", valorIntereses)
print("Descuento por retención en la fuente (7%): $", retencion)
print("Valor total a retirar al final del periodo: $", valorTotalRetirar)
print("----------------------------------------")