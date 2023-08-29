import random

numero=random.randint(1,20)
jugar=int(input("Numero 1 al 20: "))
if jugar==numero:
    print("Adivinaste, mi numero era "+str(numero))
contador=0
while jugar!=numero and contador<4:
    if jugar<numero:
        print("el numero es mayor")
        jugar=int(input("Numero 1 al 20: "))
        if jugar==numero:
            print("Adivinaste, mi numero era "+str(numero))
            break
    if jugar>numero:
        print("el numero es menor")
        jugar=int(input("Numero 1 al 20: "))
        if jugar==numero:
            print("Adivinaste, mi numero era "+str(numero))
            break
    contador+=1
    if contador==4:
        print("No adivinaste, mi número era "+str(numero))