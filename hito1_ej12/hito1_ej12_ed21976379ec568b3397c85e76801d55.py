import random

x=random.randint(1,20)

intentos=0
while(intentos<=5):

    adivina=int(input("estoy pensando en un numero adivina en cual es: "))
    if(adivina==x):
        print("Adivinaste, mi número era ",x)
        break
    if(adivina<x):
        print("mi número es mayor")
        intentos=intentos+1
    if(adivina>x):
        print(" mi número es menor")
        intentos=intentos+1
    if(intentos==5):
        print("No adivinaste, mi número era",x)
        break
      