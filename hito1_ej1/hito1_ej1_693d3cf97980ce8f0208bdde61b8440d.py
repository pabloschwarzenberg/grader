#Nota final
pt=float(input("ingrese notas de tareas: "))
pi=float(input("ingrese notas de interrogaciones: "))
ne=float(input("ingrese notas de examen: "))
pp=float(input("ingrese notas de presentacion: "))

promedio=(0.3*pt)+(0.3*pi)+(0.3*ne)+(0.1*pp)
promedio_aproximado= round(promedio, 1)
print(promedio_aproximado)     