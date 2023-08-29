#Sistema de Ecuaciones
 def solucion_ecuacion(a,b,c,d,e,f):
    xd = a*e - b*d
    if xd != 0:
        x = (e*c - f*b)/ xd
        y = (a*f - d*c)/ xd

        return x, y
    else:
        print(0)
        