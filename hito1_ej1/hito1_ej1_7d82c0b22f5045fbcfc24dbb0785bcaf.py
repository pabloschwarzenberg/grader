#Nota final
pt = float(input("Ingrese la nota de su tarea: "))
pi = float(input("Ingrese la nota de su interrogacion: "))
ne = float(input("Ingrese la nota de su examen: "))
pp = float(input("Ingrese su nota de presentación: "))

promedio = (0.3 * pt) + (0.3 * pi) + (0.3 * ne) + (0.1 * pp)

n_final = round(promedio, 1)

print("Su promedio final es:", n_final)

