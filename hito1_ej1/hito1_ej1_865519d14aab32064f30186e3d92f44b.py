#Nota final
pt = float(input("ingrese la nota de tareas: "))
pi = float(input("ingrese la nota de interrogaciones: "))
ne = float(input("ingrese la nota de examen: "))
pp = float(input("ingrese la nota de presentacion: "))
pf = round((0.3 * pt) + (0.3 * pi) + (0.3 * ne) + (0.1 * pp), 1)
print("su primedio final es: %.1f " %(pf))