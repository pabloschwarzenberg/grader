#Juego adivina mi número
from random import *
ra=randint(1,20)
for n in range(6):
    if n==5:
        print("No, mi numero era:",ra)
        break
    elif n<5:
        y=int(input("Numero: "))
        if y==ra:
            print("Adivinaste, mi numero era:",ra)
            break
        elif y>ra:
            print("Mi numero es menor que el tuyo")
        else:
            print("Mi numero es mayor que el tuyo")
      