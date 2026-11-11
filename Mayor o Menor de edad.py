# Definición de variables y lectura de datos
nombre = input("Ingresa tu nombre: ")
edad_persona = float(input("Ingresa tu edad: "))

# Condicional para verificar la mayoría de edad
if edad_persona > 18:
    print("¡Felicitaciones! Eres mayor de edad, vamos por una pola")
else:
    print("Lo siento, aun no puedes tomar legalmente")