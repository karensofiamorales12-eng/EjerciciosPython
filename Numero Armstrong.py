# Ejercicio: Verificador de números de Armstrong

respuesta = "S"

while respuesta == "S" or respuesta == "s":
    print("--- VERIFICADOR DE NÚMEROS DE ARMSTRONG ---")
    num = int(input("Ingrese un número entero positivo en base 10: "))
    
    if num > 0:
        # 1. Contar la cantidad de cifras o dígitos del número (n)
        temp = num
        n = 0
        while temp > 0:
            temp = temp // 10
            n += 1
            
        # 2. Calcular la suma de cada cifra elevada a la potencia n
        temp = num
        suma = 0
        while temp > 0:
            digito = temp % 10
            suma += digito ** n
            temp = temp // 10
            
        # 3. Informar si el resultado es o no un número de Armstrong
        if suma == num:
            print("El número ", num, " SÍ es un número de Armstrong.")
        else:
            print("El número ", num, " NO es un número de Armstrong.")
    else:
        print("Por favor, ingrese un número entero positivo válido.")
        
    print()
    respuesta = input("¿Desea evaluar otro número? (S/N): ")

print("¡Programa finalizado!")