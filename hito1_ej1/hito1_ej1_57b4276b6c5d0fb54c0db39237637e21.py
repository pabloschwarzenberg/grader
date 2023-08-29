#Nota final

PT = float(input("Ingrese promedio tareas: "))
PI = float(input("Ingrese promedio interrogaciones: "))
NE = float(input("Ingrese nota examen: "))
PP = float(input("Ingrese nota presentación: "))

promedioFinal = PT*.3+PI*.3+NE*.3+PP*.1

print(round(promedioFinal,1))