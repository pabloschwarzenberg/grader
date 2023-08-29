#Sistema de Ecuaciones
def solucion_sistemas_ecuaciones (a, b, c, d, e, f):
    determinante = a*e - b*d

    if determinante != 0:
      x= (c*e - b*f) / determinante
      y= (a*f - c*d) / determinante

      return x,y
    else:
        return None, None

a,b,c,d,e,f = 2,3,6,1,2,5

print(solucion_sistemas_ecuaciones(a,b,c,d,e,f))