#Nota final
PT = float(input("Ingrese la nota de sus tareas: "))
PI = float(input("Ingrese la nota de sus interrogaciones: "))
N3 = float(input("Ingrese la nota de su examen: "))
PP = float(input("Ingrese la nota de presentanción: "))

print()

promedio = 0.3*PT + 0.3*PI + 0.3*N3 + 0.1*PP

promedior = round(promedio, 1)

print(promedior)      