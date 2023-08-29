#Ordenar tres números
x = int(input("ingrese un numero "))
x1 = int(input("ingrese un numero "))
x2 = int(input("ingrese un numero "))
if x < x1 and x < x2:
    if x1< x2:
        print(x,",",x1,",",x2)
    else:
        print(x,",",x2,",",x1)
if x1 < x and x1 < x2:
    if x < x2:
        print(x1,",",x,",",x2)
    else:
        print(x1,",",x2,",",x)
if x2 < x1 and x2< x:
    if x1< x:
        print(x2,",",x1,",",x)
    else:
        print(x2,",",x,",",x1)