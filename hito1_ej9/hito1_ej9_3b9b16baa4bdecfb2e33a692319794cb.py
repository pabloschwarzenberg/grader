#Sistema de Ecuacion
a=float(input())
b=float(input())
c=float(input())
d=float(input())
e=float(input())
f=float(input())

y=(f*a-d*c)/(a*e-d*b)
x=(c-b*y)/a

print("x=", round(x,1))
print("y=", round(y,1))

