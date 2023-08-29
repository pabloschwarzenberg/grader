#Sistema de Ecuaciones
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
det = a*e - b*d
if det != 0:
    x = (c*e - b*f)/det
    y = (a*f - c*d)/det
    print('x=',x)
    print('y=',y)
else:
    print('Sin Soluciones')      