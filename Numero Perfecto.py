# Ejercicio: Verificador de números perfectos

respuesta = "S"

while respuesta == "S" or respuesta == "s":
    print("--- VERIFICADOR DE NÚMEROS PERFECTOS ---")
    num = int(input("Ingrese un número entero positivo: "))
    
    if num > 0:
        suma = 0
        
        # Encontrar y sumar los divisores propios positivos
        for i in range(1, num):
            if num % i == 0:
                suma += i
                
        # Comprobar si el número es perfecto (igual a la suma de sus divisores propios)
        if suma == num:
            print("El número ", num, " SÍ es un número perfecto.")
        else:
            print("El número ", num, " NO es un número perfecto.")
    else:
        print("Por favor, ingrese un número entero positivo válido.")
        
    print()
    respuesta = input("¿Desea evaluar otro número? (S/N): ")

print("¡Programa finalizado!")