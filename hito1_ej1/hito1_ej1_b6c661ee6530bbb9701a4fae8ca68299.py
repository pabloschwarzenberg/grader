#Nota final
PT = float(input("Ingrese la nota tareas: "))
PI = float(input("Ingrese la nota interrogaciónes: "))
NE = float(input("Ingrese la nota examen: "))
PP = float(input("Ingrese la nota presentación: "))

promedioFinal = (0.3 * PT) + (0.3 * PI) + (0.3 * NE) + (0.1 * PP)

print(round(promedioFinal, 1))