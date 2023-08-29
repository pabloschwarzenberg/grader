PT = float(input("ingrese promedio de las tareas: "))
PI = float(input("ingrese promedio de las interrogaciones: "))
NE = float(input("ingrese nota del examen: "))
PP = float(input("ingrese nota de presentación: "))

NF = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP


print(round(NF, 1))