#Nota final
pt=float(input("ingrese nota de tareas"))
pi=float(input("ingrese nota de interrogantes"))
ne=float(input("ingrese nota de examen"))
pp=float(input("ingrese nota de presentacion"))
n1=0.3*pt
n2=0.3*pi
n3=0.3*ne
n4=0.1*pp
notafinal=round(n1+n2+n3+n4,1)
print("el resultado final es:", notafinal)
