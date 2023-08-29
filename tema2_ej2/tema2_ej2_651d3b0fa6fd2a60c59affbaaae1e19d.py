a=int()
b=int()
def amigos(a,b):
    suma_1=0        
    suma_2=0
    contador_1=0
    contador_2=0
    while (contador_1<(a-1)):
        contador_1=contador_1+1
        if (a%contador_1 == 0):
            suma_1=suma_1+contador_1
    while (contador_2<(b-1)):
        contador_2=contador_2+1
        if (b%contador_2 == 0):
            suma_2=suma_2+contador_2
    print (suma_1)
    print (suma_2)
    if (suma_1 == b and suma_2 == a):
        print (True)
        return (True)
    else: 
        print (False)
        return (False)
amigos(a,b)