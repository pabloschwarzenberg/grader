import random
Intento = 0
Incog = int(random.randrange(20))
while not (Incog == 0):
    Intento = Intento + 1
    if Intento <=5 :
        Numero = int(input("Adivine el Número del 1 al 20: "))
        if Incog < Numero:
            print("mi número es menor")
        elif Incog > Numero:
            print("mi número es mayor")
        elif Incog == Numero:
            print("Adivinaste, mi número era: ",Incog)
            break
    else:
        print("No adivinaste, mi número era: ",Incog)
        break