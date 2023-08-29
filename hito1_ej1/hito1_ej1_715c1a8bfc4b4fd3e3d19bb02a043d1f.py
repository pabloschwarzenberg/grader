#Nota final
pt = float(input("Ingrese la nota de las tareas: "))       
pi = float(input("Ingrese la nota de las interrogaciones: "))
ne = float(input("Ingrese la nota del examen: "))
pp = float(input("Ingrese la nota de la presentación: "))

promediof = 0.3* pt + 0.3 * pi + 0.3 * ne + 0.1 * pp
promfredon = round(promediof, 1)
print(promfredon)