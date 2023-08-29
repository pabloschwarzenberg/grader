pt=float(input("Nota tareas: "))
pi=float(input("Nota interrogaciones: "))
ne=float(input("Nota examen: "))
pp=float(input("Nota presentación: "))

x=(0.3*pt)+(0.3*pi)+(0.3*ne)+(0.1*pp)
y=round(x,1)
print("Promedio: {}".format(y))


      