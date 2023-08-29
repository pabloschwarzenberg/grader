from random import *
n=randint(1,20)
for x in range(6):
    if x==5:
        print("No adivinaste, Mi numero era:",n)
        break
    elif x<5:
        u=int(input("Numero: "))
        if u==n:
            print("Adivinaste, mi numero era:",n)
            break
        elif u>n:
            print("Mi numero es menor que el tuyo")
        else:
            print("Mi numero es mayor que el tuyo")
