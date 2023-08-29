#Nota final
pt=float(input("Escriba su nota de tareas: "))
pi=float(input("Escriba su nota de interrogaciones: "))
ne=float(input("Escriba su nota del examen: "))
pp=float(input("Escriba su nota de presentacion: "))
n1=0.3*pt
n2=0.3*pi
n3=0.3*ne
n4=0.1*pp
notafinal=round(n1+n2+n3+n4,1) 
print("Tu promedio final es: ",notafinal)     