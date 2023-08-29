#Juego adivina mi número
import random
a = 0
A = int(random.randrange(20))
while not (A == 0):
    a = a + 1
    if a <=5 :
        B = int(input("Adivine el Número del 1 al 20: "))
        if A < B:
            print("mi número es menor")
        elif A > B:
            print("mi número es mayor")
        elif A == B:
            print("Adivinaste, mi número era: ", A)
            break
    else:
        print("No adivinaste, mi número era: ",A)
        break      