#Nota final
pt = float(input("Nota de tareas: "))
pi = float(input("Nota de interrogaciones: "))
ne = float(input("Nota del examen: "))
pp = float(input("Nota de presentación: "))

pf = 0.3 * pt + 0.3 * pi + 0.3 * ne + 0.1 * pp
print(round(pf, 1))