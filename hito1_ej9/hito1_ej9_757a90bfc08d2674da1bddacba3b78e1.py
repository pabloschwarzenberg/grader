def solucion_sistema_ecuaciones(a,b,c,d,e,f):
    determinante=a*e-b*d
    if determinante!=0:
        x=(c*e-b*f)/determinante
        y=(a*f-c*d)/determinante
        x= round(x,1)
        y= round(y,1)
        rx= 'x=%s'% (str(x))
        ry= 'y=%s'% (str(y))
        lista=[rx,ry]
        return print(lista)
    else:
        return None,None
a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
f=int(input())
solucion_sistema_ecuaciones(a,b,c,d,e,f)