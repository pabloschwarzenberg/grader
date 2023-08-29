#Sistema de Ecuaciones
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())

if a != 0 and d*b != a*e:
    y = (d*c-f*a)/(d*b - a*e)
    x = (c - b*y)/a



print('x=', round(x,1),', y=', round(y,1))    