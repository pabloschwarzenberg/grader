import random
n=1
numero=random.randint(1,20)
while 1<=n<=5:
    print("Estoy pensando en un numero del 1 al 20")
    print("¿Cuál es?")
    eleccion=int(input())
    if eleccion==numero:
        print("adivinaste, mi numero era ",numero)
        n=7
    else:
        #print("no adivinaste")
        if eleccion<numero:
            print("mi numero es mayor que el que elegiste")
            n=n+1
        elif eleccion>numero:
            print("mi numero es menor que el que elegiste")
            n=n+1
while n==6:
    print("no adivinaste, mi numero era ",numero)
    n=7
        