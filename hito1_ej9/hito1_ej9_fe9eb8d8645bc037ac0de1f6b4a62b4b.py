#Sistema de Ecuaciones
instruccion="Escribir el sistema de ecuaciones de la forma ax+by=c,dx+ey=f"
print(instruccion)
a=float(input("término a:"))
b=float(input("término b:"))
c=float(input("término c:"))
d=float(input("término d:"))
e=float(input("término e:"))
f=float(input("término f:"))
valorcalculadodey=(c*d-a*f)/(b*d-a*e)
valorcalculadodex=(c*e-b*f)/(a*e-b*d)
print("x=",valorcalculadodex)
print("y=",valorcalculadodey)