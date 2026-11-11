# Ejercicio: Convertir centímetros a yardas, metros, pies y pulgadas
cm = float(input("Ingrese la cantidad en centímetros: "))

# Fórmulas de conversión
metros = cm / 100
pulgadas = cm / 2.54
pies = cm / 30.48
yardas = cm / 91.44

# Mostrar los resultados en pantalla
print("----------------------------------------")
print("Equivalencias para ", cm, " cm:")
print("Metros: ", metros)
print("Pulgadas: ", pulgadas)
print("Pies: ", pies)
print("Yardas: ", yardas)
print("----------------------------------------")