#Sistema de Ecuaciones
A="ax+by=c"
B="dx+ey=f"
A=print(A)
B=print(B)
a=float(input("a:"))
b=float(input("b:"))
c=float(input("c:"))
d=float(input("d:"))
e=float(input("e:"))
f=float(input("f:"))
g=c*e-b*f
h=a*e-b*d
i=a*f-c*d
j=a*e-b*d
k=a/b
l=d/e
if(k==l):
    Nosolucion=print("EL SISTEMA NO TIENE UNA SOLUCION UNICA")
if(k!=l):
    solucionx=print("x=",g/h)
    soluciony=print("y=",i/j)
