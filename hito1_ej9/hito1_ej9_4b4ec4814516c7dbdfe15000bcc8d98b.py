#Sistema de Ecuaciones
a=float(input("Ingrese el término que acompaña a x en la primera ecuacion: "))
b=float(input("Ingrese el término que acompaña a y en la primera ecuacion: "))
c=float(input("Ingrese el término libre de la primera ecuacion: "))
d=float(input("Ingrese el término que acompaña a x en la segunda ecuacion: "))
e=float(input("Ingrese el término que acompaña a y en la segunda ecuacion: "))
f=float(input("Ingrese el término libre de la segunda ecuacion: "))

y=(c*d-a*f)/(b*d-a*e)
x=(c*e-f*b)/(a*e-b*d)

print("x=",x)
print("y=",y)     