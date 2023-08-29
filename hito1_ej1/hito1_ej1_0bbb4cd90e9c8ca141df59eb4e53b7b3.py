#Nota final
pt=float(input("Ingrese la nota de tareas: "))
pi=float(input("Ingrese la nota de interrogación: "))
ne=float(input("Ingrese la nota de examen: "))
pp=float(input("Ingrese la nota de presentación: "))

promedio=(0.3*pt)+(0.3*pi)+(0.3*ne)+(0.1*pp)

print("El promedio es: " + str(round(promedio,1)))