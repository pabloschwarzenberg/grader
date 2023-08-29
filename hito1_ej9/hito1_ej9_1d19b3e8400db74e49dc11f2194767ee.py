#Sistema de Ecuaciones
def sistema_ecuaciones(a1,b1,c1,a2,b2,c2):
    determinante=(a1*b2)-(a2*b1)

    if determinante==0:
        print("El sistema no tiene una unica solucion")
    else:
        x=((c1*b2)-(c2*b1))/determinante
        y=((a1*c2)-(a2*c1))/determinante
        #print("x="+ str(round(x,1)))
        #print("y="+ str(round(y,1)))
    print(['x=' + str(round(x, 1)), 'y=' + str(round(y, 1))])
a1=int(input("Ingrese la variable a de la primera ecuacion: "))
b1=int(input("Ingrese la variable b de la primera ecuacion: "))
c1=int(input("Ingrese la variable c de la primera ecuacion: "))
a2=int(input("Ingrese la variable a de la segunda ecuacion: "))
b2=int(input("Ingrese la variable b de la segunda ecuacion: "))
c2=int(input("Ingrese la variable c de la segunda ecuacion: "))
sistema_ecuaciones(a1,b1,c1,a2,b2,c2)

  