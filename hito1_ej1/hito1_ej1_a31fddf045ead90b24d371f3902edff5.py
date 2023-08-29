#Nota final
pt = float(input("Ingrese la nota de tareas: "))
pi = float(input("Ingrese la nota de integraciones: "))
ne = float(input("Ingrese la nota del examen: "))
pp = float(input("Ingrese la nota de presentacion: "))

pf = (0.3*pt + 0.3*pi + 0.3*ne + 0.1*pp)


print(round(pf))
