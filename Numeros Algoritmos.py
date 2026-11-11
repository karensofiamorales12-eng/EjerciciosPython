# Ejercicio: Contar y sumar las cifras de un número entero positivo
num = int(input("Escriba un número entero: "))

if num > 0:
    copiaNumero = num
    contadorCifras = 0
    sumaCifras = 0
    
    while copiaNumero > 0:
        cifra = copiaNumero % 10
        copiaNumero = copiaNumero // 10
        sumaCifras += cifra
        contadorCifras += 1
        
    print("El numero ingresado es: ", num)
    print("La cantidad de cifras es: ", contadorCifras)
    print("La sumatoria es:", sumaCifras)
else:
    print("No es un número positivo")