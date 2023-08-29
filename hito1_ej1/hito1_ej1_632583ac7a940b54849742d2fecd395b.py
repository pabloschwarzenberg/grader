#Nota final
pt = float(input("inserte las notas de tareas: "))
pi = float(input("inserte las notas de interrogantes: "))
ne = float(input("inserte las notas de examen: "))
pp = float(input("inserte las notas de presentacion: "))

pf = 0.3 * pt + 0.3 * pi + 0.3 * ne + 0.1 * pp
redondeado = round(pf, 1)
print("el promedio final resulta ", redondeado)