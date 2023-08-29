#Sistema de Ecuaciones
a =float(input())
b =float(input())
c =float(input())
d =float(input())
e =float(input())
f =float(input())
y=(f*a-d*c)/(a*e-d*b)
x=(c-b*y)/a
z=round(x,1)
w=round(y,1)
print("x=",z)
print("y=",w) 