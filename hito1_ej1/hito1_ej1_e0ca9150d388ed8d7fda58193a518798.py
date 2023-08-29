pt = float(input("Ingrese nota de las Tareas: "))
pi = float(input("Ingrese nota de las Interrogaciones: "))
ne = float(input("Ingrese nota del Examen: "))
pp = float(input("Ingrese nota de la Presentacion: "))

promedio = 0.3*pt + 0.3*pi + 0.3*ne + 0.1*pp

print(round(promedio, 1))