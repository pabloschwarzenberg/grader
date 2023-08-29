#Sistema de Ecuaciones
a=float(input())
b=float(input())
c=float(input())
d=float(input())
e=float(input())
f=float(input())

det=a*e-b*d

if det!=0:
        x=(c*e-b*f)/det
        y=(a*f-c*d)/det

        print("x=",round(x,1))
        print("y=",round(y,1))
              