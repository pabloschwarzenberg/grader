#Sistema de Ecuaciones
a=float(input())
b=float(input())
c=float(input())
d=float(input())
e=float(input())
f=float(input())
x=(c*e-b*f)/(a*e-b*d)
y=(c*d-a*f)/(b*d-a*e)
print("x=",round(x,1))
print("y=",round(y,1))