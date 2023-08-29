#Nota final
pt=float(input("ingrese nota de tareas: "))
pi=float(input("ingrese nota de interrogaciones: "))
ne=float(input("ingrese nota de examen: "))
pp=float(input("ingrese nota de presentación: "))
promedio_final=(round((0.3*pt)+(0.3*pi)+(0.3*ne)+(0.1*pp),1))
print("El promedio final",promedio_final)