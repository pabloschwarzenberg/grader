#Juego adivina mi número
import random

naleatorio = random.randint(1, 20)

chances = 0

i = 1

while chances < 5 and i != 0:

    numerosec = int(input("Ingrese el numero secreto: "))

    if numerosec < naleatorio:
        print("Mi numero es mayor")
        chances += 1
        if chances == 5:
            print("No adivinaste, mi número era {}".format(naleatorio))
            i = 0

    elif numerosec > naleatorio:
        print("Mi numero es menor")
        chances += 1
        if chances == 5:
            print("No adivinaste, mi número era {}".format(naleatorio))
            i = 0

    elif numerosec == naleatorio:
        print("Adivinaste, mi número era {}".format(naleatorio))
        i = 0

    elif chances > 5:
        print("No adivinaste, mi número era {}".format(naleatorio))
        i = 0
