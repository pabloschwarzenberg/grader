#Nota final
pt = float(input("Ingrese la nota de sus Tareas: "))
pi = float(input("Ingrese la nota de sus Interrogaciones: "))
ne = float(input("Ingrese la nota de su Examen: "))
pp = float(input("Ingrese la nota de su Presentacíon: "))
promedio = (0.3 * pt) + (0.3 * pi) + (0.3 * ne) + (0.1 * pp)
aprox = round(promedio,1)
print("Su promedio es: ", aprox)