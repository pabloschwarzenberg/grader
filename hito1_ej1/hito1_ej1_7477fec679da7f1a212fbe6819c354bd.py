pt=float(input("Ingresar nota de tareas: "))
pi=float(input("Ingresar nota de interrogaciones: "))
ne=float(input("Ingresar nota de examen: "))
pp=float(input("Ingresar nota de presentación: "))
f=(0.3*pt) + (0.3*pi) + (0.3*ne) + (0.1*pp)
print("La nota final es:","{:.2}".format(f))