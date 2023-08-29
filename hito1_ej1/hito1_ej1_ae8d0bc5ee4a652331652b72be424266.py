#Nota final
pt = float(input("Ingrese nota de tareas: "))
pi = float(input("Ingrese nota de interrogaciones: "))
ne = float(input("Ingrese nota de exámen: "))
pp = float(input("Ingrese nota de presentación: "))

promedio = (0.3 * pt) + (0.3 * pi) + (0.3 * ne) + (0.1 * pp)
promedio = round(promedio, 1)

print("La nota final es:", promedio)
      