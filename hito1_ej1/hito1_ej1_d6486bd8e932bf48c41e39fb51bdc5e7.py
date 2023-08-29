PT = float(input("Ingrese la nota de las tareas: "))
PI = float(input("Ingrese la nota de las interrogaciónes: "))
NE = float(input("Ingrese la nota del examen: "))
PP = float(input("Ingrese la nota de presentación: "))
promedio_final = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
round(promedio_final)
print(promedio_final)