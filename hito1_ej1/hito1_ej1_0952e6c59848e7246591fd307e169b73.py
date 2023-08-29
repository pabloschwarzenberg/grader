#Nota final
pt = float(input("Ingrese la nota de Tareas: "))
pi = float(input("Ingrese la nota de Interrogaciones: "))
ne = float(input("Ingrese la nota de Examen: "))
pp = float(input("Ingrese la nota de Presentación: "))
promedio_final = 0.3 * pt + 0.3 * pi + 0.3 * ne + 0.1 * pp
print("El promedio final es:", round(promedio_final, 1))      