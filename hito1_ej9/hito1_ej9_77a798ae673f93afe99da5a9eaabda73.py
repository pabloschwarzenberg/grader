#Sistema de Ecuaciones
a=float(input())
b=float(input())
c=float(input())
d=float(input())
e=float(input())
f=float(input())
y=((a*f-d*c)/(a*e-d*b))
Y=round(y,1)
print("y=",Y)
x=((c-b*y)/a)
X=round(x,1)
print("x=",X)