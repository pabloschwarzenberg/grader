#Nota final
PT = float(input("Ingrese la nota de Tareas: "))
PI = float(input("Ingrese la nota de Interrogaciones: "))
NE = float(input("Ingrese la nota del Examen: "))
PP = float(input("Ingrese la nota de la Presentación: "))
promed = (0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP)
print("El promedio de notas es: " + str(round(promed, 1)))