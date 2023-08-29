#Sistema de Ecuaciones
print("Inserte valores de la ecuación 1 de la forma ax+by=c")
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
print("Inserte valores de la ecuacion 2 de la forma dx+ey=f")
d=int(input("d="))
e=int(input("d="))
f=int(input("f="))
y=((a*f-c*d)/(e*a-b*d))
x=((e*c-b*f)/(a*e-d*b))
if(a*e)==(d*b):
 print("error")
else:
 print("x=",x)
 print("y=",y)
 
