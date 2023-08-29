#Nota final
pt=float(input("ingrese el promedio de tareas:"))
pi=float(input("ingrese el promedio de interrogaciones:"))
ne=float(input("ingrese la nota del exámen:"))
pp=float(input("ingrese el promedio de la presentación:"))
x=(0.3*pt)+(0.3*pi)+(0.3*ne)+(0.1*pp)
print(round(x,1))