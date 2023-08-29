#Nota final
pt = float(input("Ingrese nota tareas: "))
pi = float(input("Ingrese nota interrogaciones: "))
ne = float(input("Ingrese nota examen: "))
pp = float(input("Ingrese nota presentacion: "))

nt = 0.3 * pt + 0.3 * pi + 0.3 * ne + 0.1 * pp
round(nt, 1)
print("La nota final es:" + str(nt))     