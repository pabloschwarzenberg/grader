#Nota final
PT=float(input("ingrese la nota de tareas:"))
PI=float(input("ingrese la nota de interrogacones:"))
NE=float(input("ingrese la nota del examen:"))
PP=float(input("ingrese la nota de presentacion:"))
prom=((0.3*PT)+(0.3*PI)+(0.3*NE)+(0.1*PP))
print("{0:1f}".format(prom))
