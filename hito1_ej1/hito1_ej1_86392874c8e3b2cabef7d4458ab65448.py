#Nota final#

pt = float(input("Ingrese nota de tareas: "))
pi = float(input("Ingrese nota de interrogaciones: "))
ne = float(input("Ingrese nota Examen: "))
pp = float(input("Ingrese nota presentación: "))

Nf = (0.3 * pt) + (0.3 * pi) + (0.3 * ne) + (0.1 * pp)

Nfr = round(Nf, 1)


print("Tu nota es:" ,Nfr)   