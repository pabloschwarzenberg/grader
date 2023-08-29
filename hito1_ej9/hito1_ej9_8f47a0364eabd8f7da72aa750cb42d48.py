#Sistema de Ecuaciones
a=float(input("Ingrese primer cofactor: "))
b=float(input("Ingrese segundo cofactor: "))
c=float(input("Ingrese tercer cofactor: "))
d=float(input("Ingrese primer cofactor: "))
e=float(input("Ingrese segundo cofactor: "))
f=float(input("Ingrese tercer cofactor: "))

x=(b*f-c*a)/(b*d-e*a)
y=(d*c-a*f)/(d*b-a*e)

if (b*d-e*a)!=0 and (d*b-a*e):
 print("x=",x)
 print("y=",y)
else:
 print("Sistema no tiene solución")