#Nota final
pt = float(input("Ingresa tu nota de tareas: "))
pi = float(input("Ingresa tu nota de interrogaciones: "))
ne = float(input("Ingresa tu nota de examen: "))
pp = float(input("Ingresa tu nota de presentacion: "))

pf = (0.3 * pt) + (0.3 * pi) + (0.3 * ne) + (0.1 * pp)

print('Tu promedio final es'+str(round(pf, 1)))
