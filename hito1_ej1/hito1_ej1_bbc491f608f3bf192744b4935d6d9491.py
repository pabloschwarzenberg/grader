#Nota final
pt = float(input("Ingrese la nota de las tareas: "))
pi = float(input("Ingrese la nota de las interrogaciones: "))
ne = float(input("Ingrese la nota de las examen: "))
pp = float(input("Ingrese la nota de las presentacion: "))

promedioFinal = (0.3 * pt) + (0.3 * pi) + (0.3 * ne) + (0.1 * pp)
pfRedondeado = round(promedioFinal, 1)

print(pfRedondeado)