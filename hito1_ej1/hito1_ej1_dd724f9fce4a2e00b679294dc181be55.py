#Nota final
PT = float(input("Ingrese la nota de su tarea: "))
PI = float(input("Ingrese la nota de la interrogacion: "))
NE = float(input("Ingrese la nota de su examen: "))
PP = float(input("Ingrese la nota de su presentacion: "))

#Promedio
Med = round(float(0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP),1)
#Muestra promedio
print("El promedio es: ", Med)
      