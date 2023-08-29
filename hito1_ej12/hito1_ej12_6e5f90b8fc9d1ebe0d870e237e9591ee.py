#Juego adivina mi número
import random
numero=random.randint(1,20)

print("ingrese un numero del 1 al 20 ")
a=int(input())

if(numero==a):
    print("adivisnaste, mi número era",numero)
else:
    if(numero>a):
        print("mas arriba")

    else:
        if(numero<a):
            print("mas Abajo")

b=int(input())

if(numero==b):
    print("adivisnaste, mi número era",numero)
else:
    if(numero>b):
        print("mas arriba")

    else:
        if(numero<b):
         print("mas abajo")

c=int(input())

if(numero==c):
    print("adivisnaste, mi número era",numero)
else:
    if(numero>c):
        print("mas arria")

    else:
        if(numero<c):
         print("mas abajo")

d=int(input())

if(numero==d):
    print("adivisnaste, mi número era",numero)
else:
    if(numero>d):
        print("mas arria")

    else:
        if(numero<d):
         print("mas abajo")

        
b=int(input())

if(numero==b):
    print("adivinaste")
else:
            print("no adivinaste,mi numero era",numero)