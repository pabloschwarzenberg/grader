#Juego adivina mi número
import random
x=(random.randint(1,20))
n=0
while n<5:
    numero=int(input())
    
    if numero==x:
        print("Adivinaste, mi número era "+str(x))
    else:
        if numero>x:
            print("mi número es menor")
        elif numero<x:
            print("mi número es mayor")
    n=n+1
print( "No adivinaste, mi número era "+str(x))
    