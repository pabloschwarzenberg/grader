def respuesta(x1,y1,c1,x2,y2,c2):
    determinante = x1*y2-y1*x2
    if determinante != 0:
        X = (c1*y2 - y1*c2)/ determinante
        Y = (x1*c2 - c1*x2)/ determinante
        return(X,Y)

    else:
        return("No hay")

x1 = float(input("Menciona el numero : "))
y1 = float(input("Menciona el numero :"))
c1  =float(input("Menciona el numero : "))
x2 = float(input("Menciona el numero : "))
y2  =float(input("Menciona el numero : "))
c2  = float(input("Menciona el numero  ;"))

resultado  = respuesta(x1,y1,c1,x2,y2,c2)
indice = 0
lista = []

for numero in resultado:
    if indice == 0:
        print("x=" , end="")

    else:
        print("y = " , end="")

    print(numero)
    indice += 1
