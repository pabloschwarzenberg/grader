#Nota final
pt=float(input("Ingrese la nota de su Tarea: "))
pi=float(input("Ingrese la nota de su Interrogacion: "))
ne=float(input("Ingrese la nota de su Examen: "))
pp=float(input("Ingrese la nota de su Presentacion"))

promedio = (0.3 * pt) + (0.3 * pi) + (0.3 * ne) + (0.1 * pp)
print(round(promedio,1))