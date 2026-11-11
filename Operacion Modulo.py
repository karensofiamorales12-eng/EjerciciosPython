# Ejercicio: Calcular el módulo (residuo de la división) entre dos números
num1 = float(input("Ingrese el primer número (dividendo): "))
num2 = float(input("Ingrese el segundo número (divisor): "))

# Validar que el divisor no sea cero para evitar errores matemáticos
if num2 != 0:
    # En Python la operación módulo se representa con el operador '%'
    resultadoModulo = num1 % num2
    
    print("----------------------------------------")
    print("El módulo de ", num1, " entre ", num2, " es: ", resultadoModulo)
    print("----------------------------------------")
else:
    print("Error: No se puede calcular el módulo dividiendo entre cero.")