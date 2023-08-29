#Nota final
pt = float(input("Ingrese el promedio de las tareas: "))
pi = float(input("Ingrese el promedio de las interrogaciones: "))
ne = float(input("Ingrese la nota de examen: "))
pp = float(input("Ingrese nota de presentacion: "))
prom = (0.3 * pt) + (0.3 * pi) + (0.3 * ne) + (0.1 * pp)
prom_round = round(prom,1)
print("Su promedio es de: ", prom_round)      