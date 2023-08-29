#Nota final
PT = float(input("Ingrese la nota de las Tareas: "))
PI = float(input("Ingrese la nota de las Interrogaciones: "))
NE = float(input("Ingrese la nota del Examen: "))
PP = float(input("Ingrese la nota de Presentacion: "))

PF = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP

print("El promedio final de las notas es: ",round(PF,1))
