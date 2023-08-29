#Nota final
# entrada

PT = float(input("Ingrese la nota de su tarea "))
PI = float(input("Ingrese la nota de sus interrogaciones  "))
NE = float(input("Ingrese la nota de su examen "))
PP = float(input("Ingrese la nota de su presentación "))

# Procesamiento

promedio = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP

# Salida
print("Su promedio final es " + str(round(promedio, 1)))
      