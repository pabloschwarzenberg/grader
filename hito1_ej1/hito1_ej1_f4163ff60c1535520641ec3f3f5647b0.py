#Nota final
pt = float(input("Ingrese nota de tareas: "))
pi = float(input("Ingrese nota de interrogaciones: "))
ne = float(input("Ingrese nota de examen: "))
pp = float(input("Ingrese nota de presentacion: "))

promedio = 0.3*pt + 0.3*pi + 0.3*ne + 0.1*pp
print(round(promedio, 1))