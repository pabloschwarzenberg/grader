#Sistema de Ecuaciones
def solucion_sistema_ecuacionnes(a,b,c,d,f):
    determinante=a*e-b*d
    if determiante!=0:
       x=(c*e-b*f)/determinante
       y=(a*f-c*d)/determinante
       print (x,y)
     