pt=float(input("ingresar nota de tareas: "))
pi=float(input("ingresar nota de interrogaciones: "))
ne=float(input("ingrese mota de examen: "))
pp=float(input("ingrese nota de presentación: "))

Promedio = float(((0.3 * pt) + (0.3 * pi) + (0.3 * ne) + (0.1 * pp)))

print(round(Promedio,1))