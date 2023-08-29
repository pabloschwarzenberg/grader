#Nota final
pt = float(input("Ingrese la nota de sus tareas: "))
pi = float(input("Ingrese la nota de sus interrogaciones: "))
ne = float(input("Ingrese la nota de su examen: "))
pp = float(input("Ingrese la nota de su presentacion: "))

prom = (0.3 * pt) + (0.3 * pi) + (0.3 * ne) + (0.1 * pp)
promred = round(prom,1)

print("Su promedio final es:",promred)