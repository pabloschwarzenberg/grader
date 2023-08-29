#Sistema de Ecuaciones
def solucion_sisX(a,b,c,d,e,f):
    determinante = a*e - b*d
    if determinante != 0:
        x = (c*e - b*f)/ determinante
        return x
        
    else:
        return None, None
def solucion_sisY(a,b,c,d,e,f):
    determinante = a*e - b*d
    if determinante != 0:
        y = (a*f - c*d)/ determinante
        return y
a,b,c,d,e,f = map(float, input().split())
respuesta=("[x=",solucion_sisX(a, b, c, d, e, f),"y=",solucion_sisY(a,b,c,d,e,f),"]")
print(respuesta)