#Juego adivina mi número
from random import*
num=randint(1,20)
n=0
while(n<5):
    respuesta=int(input("Cual crees que es el numero?:" ))
    if (respuesta!=num):
        n=n+1
        if(respuesta>num):
            print("Te has equivocado, el numero que dices es mayor")
        else:
            print("Te has equivocado, el numero que dices es menor")
    else:
        print("Adivinaste, mi número era",num)
        n=6
if(n!=6):
    print("No adivinaste, mi número era",num)      