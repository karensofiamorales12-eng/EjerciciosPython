# Ejercicio: Calcular el salario total a partir de las horas laboradas y el valor de la hora
horasTrabajadas = float(input("Ingrese el número de horas laboradas durante el periodo: "))
valorHora = float(input("Ingrese el valor que se paga por cada hora: "))

# Operación para calcular el salario total
salarioTotal = horasTrabajadas * valorHora

# Mostrar el resultado en pantalla
print("El salario total a pagar al empleado es: $", salarioTotal)