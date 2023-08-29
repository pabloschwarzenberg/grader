#Nota final
pt = float(input("ingrese las notas de las tareas : "))
pi = float(input("ingrese las notas de las interrogaciones : "))
ne = float(input("ingrese la nota del examen : "))
pp = float(input("ingrese la nota de presentacion : "))
promedio = 0.3 * pt + 0.3 * pi + 0.3 * ne + 0.1 * pp
print("{0:1f}".format(promedio))