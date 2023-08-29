#Nota final
pt = float(input("Ingrese la Nota de la tarea: "))
pi = float(input("Ingrese la Nota de las interrogaciones: "))
ne = float(input("Ingrese la Nota del examen: "))
pp = float(input("Ingrese la Nota de presentacion: "))
promedio = (0.3 * pt) + (0.3 * pi) + (0.3 * ne) + (0.1 * pp)

print("Su nota final es: ", round(promedio, 1))