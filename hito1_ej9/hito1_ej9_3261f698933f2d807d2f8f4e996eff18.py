#Sistema de Ecuaciones
a=float(input("ingrese primer valor:"))
b=float(input("ingrese segundo valor:"))
c=float(input("ingrese tercer valor:"))
d=float(input("ingrese primer valor:"))
e=float(input("ingrese segundo valor:"))
f=float(input("ingrese tercer valor:"))
determinante = a*e - b*d
if determinante != 0:
    x = (c*e - b*f) / determinante
    y = (a*f - c*d) / determinante


print("x="+str(x))
print("y="+str(y))     