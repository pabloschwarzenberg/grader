#Nota final
pt=eval(input("Ingrese la nota de tareas: "))
pi=eval(input("Ingrese la nota de interrogaciones: "))
ne=eval(input("Ingrese la nota de examen: "))
pp=eval(input("Ingrese la nota de presentacion: "))
fm=(0.3*pt)+(0.3*pi)+(0.3*ne)+(0.1*pp)
print(round(fm,1))