#Nota final
pt = float(input("Ingrese su nota de Tareas: "))
pi = float(input("Ingrese su nota de Interrogaciones: "))
ne = float(input("Ingrese su nota de Examen: "))
pp = float(input("Ingrese su nota de Presentación: "))
prom = 0.3*pt + 0.3*pi + 0.3*ne + 0.1*pp

print(f"Su promedio final es ""{:.1f}".format(prom))