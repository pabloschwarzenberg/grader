#Sistema de Ecuaciones
 def solucion_sistema_ecuaciones(a, b, c, d ,e ,f):
    determinar= a*e - b*d

    if determinar !=0:
        x= ( c*e - b*f)/determinar
        y= (a*f - c*d)/determinar
        return x, y
    else:
        return None,None

    print(' digitar valores para a, b, c, d, e, f :')
    a, b, c, d, e, f, = map(float, input().split())

    print(solucion_sistema_ecuaciones(a,b,c,d,e,f,))