tp = float(input("ingresa la nota de tarea: "))
pi = float(input("ingresa la nota de interrogaciones: "))
ne = float(input("ingresa la nota de examen: "))
pp = float(input("ingresa la nota de presentaciones: "))
print()
suma = tp + pi + ne + pp
promedio = suma / 4
print(round(promedio,1))      