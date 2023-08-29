import random
n=random.randint(1,20)
intentos=0
jugar=True
print("adivina el numero del 1 al 20 ")
while jugar:
    intentos +=1
    if intentos <=5:
        elije= int(input("elije un numero:"))
        if elije==n:
            print("has adivinado. necesitaste", intentos, "intentos.")
            jugar=False
        elif elije>n:
            print("demasiado alto. llevas", intentos,"intentos.")
        elif elije<n:
            print("demasiado bajo. llevas", intentos,"intentos.")
    else:
        print("se te acabaromn los intentos. no adivinaste.")
        jugar =False
            