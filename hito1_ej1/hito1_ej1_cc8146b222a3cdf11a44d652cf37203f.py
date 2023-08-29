print("Ingresa las siguientes notas")

pt = float(input("Tareas: "))
pi = float(input("Interrogaciones: "))
ne = float(input("Examen: "))
pp = float(input("Presentación: "))

promedio_final = (0.3 * pt) + (0.3 * pi) + (0.3 * ne) + (0.1 * pp)

print(round(promedio_final, 1))