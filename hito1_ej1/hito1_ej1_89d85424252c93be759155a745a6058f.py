#Nota final
pt = float(input('Ingrese la nota de Tareas'))
pi = float(input('Ingrese la nota de Interrogaciones'))
ne = float(input('Ingrese la nota del examen'))
pp = float(input('Ingrese la nota de presentacion'))

result = (0.3 * pt) + (0.3 * pi) + (0.3 * ne) + (0.1 * pp)
print(round(result, 1))