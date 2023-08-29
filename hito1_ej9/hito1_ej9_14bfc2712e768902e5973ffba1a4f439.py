#Sistema de Ecuaciones
a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
f=int(input())
y=((d*c)-(a*f))/((d*b)-(a*e))
x=(c-b*y)/a
print('x=', round(x, 1))
print('y=', round(y, 1))