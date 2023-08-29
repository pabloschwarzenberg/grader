#Nota final


PT = float(input("Su nota de Tareas: "))
PI = float(input("Su nota de Interrogaciones: "))
NE = float(input("Su nota de Examen: "))
PP = float(input("Su nota de Presentación: "))

promedio = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP

print(round(promedio,1))