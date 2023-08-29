#Sistema de Ecuaciones
a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

discr = a * e - b * d

if discr != 0 :
    x = (e * c - b * f) / discr
    y = (a * f - d * c) / discr

    print('x=',x)
    print('y=',y)

else :
    m = d / a

    if m * c == f :
        print("El sistema tiene infinitas soluciones")
    else:
        print("El sistema no tiene soluciones")     