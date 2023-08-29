#Nota final
pt = float(input("ingrese su nota de tareas: "))
pi = float(input("ingrese su nota de interrogaciones: "))
pe = float(input("ingrese su nota de examen: "))
pp = float(input("ingrese su nota de presentacion: "))
n1= 0.3*pt
n2= 0.3*pi
n3= 0.3*pe
n4= 0.1*pp
promedio= n1+n2+n3+n4
print("su promedio es", round(promedio,1))