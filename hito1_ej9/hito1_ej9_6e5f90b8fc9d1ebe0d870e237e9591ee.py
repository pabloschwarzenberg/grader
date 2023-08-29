#Sistema de Ecuaciones
a=float(input())
b=float(input())
c=float(input())
d=float(input())
e=float(input())
f=float(input())

m= float(a*e-b*d)
if (d!=0):
    x = ((e*c-b*f)/m)
    y = ((a*f-d*c)/m)
    print("'[x={}', 'y={}']".format(x, y))