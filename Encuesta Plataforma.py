# Ejercicio: Encuesta de preferencia de plataforma de desarrollo móvil

contAndroid = 0
contIOS = 0
respuesta = "S"

while respuesta == "S" or respuesta == "s":
    print("--- ENCUESTA: PLATAFORMA DE DESARROLLO MÓVIL ---")
    codigo = int(input("Ingrese el código del estudiante: "))
    
    print("Seleccione la plataforma de su preferencia:")
    print("1. Android")
    print("2. iOS")
    opcion = int(input("Ingrese su opción (1 o 2): "))
    
    # Evaluar la opción ingresada
    if opcion == 1:
        contAndroid += 1
        print("¡Voto registrado con éxito para Android!")
    elif opcion == 2:
        contIOS += 1
        print("¡Voto registrado con éxito para iOS!")
    else:
        print("Opción no válida. La plataforma elegida es diferente a Android o iOS, por lo tanto no será tenida en cuenta en los resultados.")
    
    print()
    respuesta = input("¿Desea registrar el voto de otro estudiante? (S/N): ")

# Mostrar resultados finales al cerrar la encuesta
print("\n--- RESULTADOS FINALES DE LA ENCUESTA ---")
print("Total de votos para Android: ", contAndroid)
print("Total de votos para iOS: ", contIOS)
print()

# Determinar ganador o empate según las reglas del problema
if contAndroid > contIOS:
    print("La plataforma elegida es: ANDROID (mayor votación).")
elif contIOS > contAndroid:
    print("La plataforma elegida es: iOS (mayor votación).")
else:
    print("Se presenta un empate en la cantidad de votos, se usará otro mecanismo de elección.")

print()
print("¡Proceso de encuesta finalizado!")