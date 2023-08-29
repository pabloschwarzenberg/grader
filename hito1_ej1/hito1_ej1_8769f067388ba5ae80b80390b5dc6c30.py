#Nota final
PT = float(input("Ingrese nota de Tareas: "))
PI = float(input("Ingrese nota de Interrogaciones: "))
NE = float(input("Ingrese nota de Examen: "))
PP = float(input("Ingrese nota de Presentación: "))
Promedio = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
print("Su promedio es de: ", round(Promedio, 1))