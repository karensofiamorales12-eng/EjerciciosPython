# Ejemplo 2.7: Cálculo de aportes a salud (4%) y pensión (4%) sobre el salario base
salarioBase = float(input("Ingrese el salario base del empleado: "))

# Cálculo de los aportes (4% cada uno)
aporteSalud = salarioBase * 0.04
aportePension = salarioBase * 0.04

# Cálculo del total de descuentos
totalDescuentos = aporteSalud + aportePension

# Cálculo del salario neto a recibir
salarioNeto = salarioBase - totalDescuentos

# Mostrar los resultados
print("----------------------------------------")
print("Aporte a Salud (4%): $", aporteSalud)
print("Aporte a Pensión (4%): $", aportePension)
print("Total deducciones: $", totalDescuentos)
print("Salario neto a recibir: $", salarioNeto)
print("----------------------------------------")