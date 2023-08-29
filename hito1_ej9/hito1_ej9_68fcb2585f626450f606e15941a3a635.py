#Sistema de Ecuaciones
a=int(input("introdusca el valor que compaña a x de la primer ecuacion"))
b=int(input("introdusca el valor que compaña a y de la primer ecuacion"))
c=int(input("introdusca la solucion de la primer ecuacion"))
d=int(input("introdusca el valor que compaña a x de la segunda ecuacion"))
e=int(input("introdusca el valor que compaña a y de la segunda ecuacion"))
f=int(input("introdusca la solucion de la segunda ecuacion"))

determinante= (a*e)-(b*d)

if determinante!=0:
    x=(c*e-b*f)/determinante
    y=(a*f-c*d)/determinante

    print("x=",x)
    print("y=",y)
else:
    print("no tiene solucion")