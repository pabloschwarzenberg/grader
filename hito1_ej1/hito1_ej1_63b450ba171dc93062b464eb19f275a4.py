#Nota final
pt = float(input("Ingrese tareas: "))
pi = float(input("Ingrese interrogaciones: "))
ne = float(input("Ingrese examen: "))
pp = float(input("Ingrese presentación: "))
promedio_final = (pt * 0.3) + (pi * 0.3) + (ne * 0.3) + (pp * 0.1)
print(round(promedio_final, 1))
