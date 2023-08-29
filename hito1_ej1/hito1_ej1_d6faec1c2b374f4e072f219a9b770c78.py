#Nota final
pt = float(input("Ingrese nota de tareas: "))
pi = float(input("Ingrese nota de interrogaciones: "))
ne = float(input("ingrese nota de examen: "))
pp = float(input("Ingrese nota de presentacion: "))
notafinal = round((0.3*pt)+(0.3*pi)+(0.3*ne)+(0.1*pp),1)
print("Su nota final es", notafinal)