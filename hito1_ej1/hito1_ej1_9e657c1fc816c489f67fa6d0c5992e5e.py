#Nota final
pt = float(input('Nota de tareas: '))
pi = float(input('Nota interrogaciones: '))
ne = float(input('Nota examen: '))
pp = float(input('Nota presentación: '))

prom = (0.3*pt)+(0.3*pi)+(0.3*ne)+(0.1*pp)
print("Nota final: {0}".format(round(prom, 1)))