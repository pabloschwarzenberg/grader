#Sistema de Ecuaciones
a=int(input())
b=int(input())
c=int(input())
d=int(input())
z=int(input())
h=int(input())
x=(h*b-d*z)/(b*c+d*a)
y=z-a*x/b
round(x,1)
round(y,1)
print(y)
print(x)
