#Nota final

pt = float(input("Ingrese nota de Tareas: "))
pi = float(input("Ingrese nota de Interrogaciones: "))
ne = float(input("Ingrese nota de Examen: "))
pp = float(input("Ingrese nota de presentación: "))

notaFinal = (0.3 * pt) + (0.3 * pi) + (0.3 * ne) + (0.1 * pp)
print(round(notaFinal, 1))