# Notafinal

print("Para calcular su prmedio final ingrese:")
pt = eval(input("Nota de tareas: "))
pi = eval(input("Nota de interrogaciones: "))
ne = eval(input("Nota de examenes: "))
pp = eval(input("Nota de presentaciones: "))
pf = round((0.3 * pt) + (0.3 * pi) + (0.3 * ne) + (0.1 * pp), 1)

print("El promedio final es: %.1f" % pf)
