#Sistema de Ecuaciones
a=float(input())
b=float(input())
c=float(input())
d=float(input())
e=float(input())
f=float(input())

y=(f*a-d*c)/(a*e-d*b)

x=(c-b*y)/a

L=round(x,1)
P=round(y,1)

print("x=",L)
print("y=",P)

if a==0 or (a*e-d*b)==0:
        print("El sistema no tiene solución")