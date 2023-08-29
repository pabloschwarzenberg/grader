#Nota final
pt = float(input("ingresa tu nota de tareas: "))
pi = float(input("ingresa tu nota de interrogaciones: "))
ne = float(input("ingresa tu nota de examen: "))
pp = float(input("ingresa tu nota de presentacion: "))
pf = 0.3 * pt + 0.3 * pi + 0.3 * ne + 0.1 * pp
print("nota final""{0:.1f}".format(pf))