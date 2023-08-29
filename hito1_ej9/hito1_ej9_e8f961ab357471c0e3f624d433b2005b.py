import math
print("digite los valores de la ecuaciones:")
a, b, c, d, e, f = map(float, input().split())
def sistema_ecuacion(a ,b ,c ,d ,e ,f):
    deteriminar =((a*e) - (b*d))

    if(deteriminar != 0):
        x=((c*e) - (b*f))/ deteriminar
        y=((a*f) - (c*d))/ deteriminar
        return x
        return y
    else:
        return None, None
print(sistema_ecuacion(a, b, c, d, e, f))