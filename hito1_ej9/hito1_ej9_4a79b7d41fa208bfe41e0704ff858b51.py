#Sistema de Ecuaciones
a=float(input())
b=float(input())
c=float(input())
d=float(input())
e=float(input())
f=float(input())
determinante = a * e - b * d
if determinante != 0 :
    x = (e * c - b * f) / determinante
    y = (a * f - d * c) / determinante
    print ("x=",x,",","y=",y)
else :
    m=d/a
    if m*c==f:
        print ("INFINITAS SOLUCIONES")
    else:
        print ("NO TIENE SOLUCION")
