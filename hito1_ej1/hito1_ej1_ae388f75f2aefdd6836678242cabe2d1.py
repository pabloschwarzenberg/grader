#Nota final
pt = float(input("Ingrese nota de tareas: "))
pi = float(input("Ingrese nota de interrogaciones: "))
ne = float(input("Ingrese nota de examen: "))
pp = float(input("Ingrese nota de presentación: "))

print( round(0.3*pt + 0.3*pi + 0.3*ne + 0.1*pp, 1) )