import random

numero=random.randint(1,20)
intentos=0

jugando=True

while jugando:
    intentos+=1

    if (intentos <=5):
        n=int(input("numero:"))
        if (n==numero):
            print("adivinaste mi numero era",numero)
            jugando=False
        elif (n<numero):
            print("mi numero es mayor")
        elif (n>numero):
            print("mi numero es menor")
    else:
        print("no adivinaste,mi numero era",numero)
        jugando=False

      