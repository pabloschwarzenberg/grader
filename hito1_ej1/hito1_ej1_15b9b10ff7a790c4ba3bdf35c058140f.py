#Nota final
from math import *

a = input("Ingrese su nota de tareas: ")
a2=float(a)

b = input("Ingrese su nota de interrogacion: ")
b2=float(b)

c = input("Ingrese su nota de examen: ")
c2=float(c)

d = input("Ingrese su nota de presentación: ")
d2=float(d)

resultado=((a2*0.3)+(b2*0.3)+(c2*0.3)+(d2*0.1))

print("Su promedio final es:%.2f"%(resultado))