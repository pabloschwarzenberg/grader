#Nota final
PT = float(input("Ingrese la nota de sus Tareas: "))
PI = float(input("Ingrese la nota de sus Interrogaciones: "))
NE = float(input("Ingrese la nota de su Examen: "))
PP = float(input("Ingrese la nota de su Presentación: "))

promedio = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
print("Su promedio es: ", promedio)     