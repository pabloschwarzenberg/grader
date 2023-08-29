#Juego adivina mi número
import random

numero=random.randint(1,20)
x=int(input("Numero 1 al 20: "))
if x==numero:
    print("Adivinaste, mi numero era "+str(x))
contador=0
while x!=numero and contador<4:
    if x<numero:
        print("el numero es mayor")
        x=int(input("Numero 1 al 20: "))
        if x==numero:
            print("Adivinaste, mi numero era "+str(x))
            break
    if x>numero:
        print("el numero es menor")
        x=int(input("Numero 1 al 20: "))
        if x==numero:
            print("Adivinaste, mi numero era "+str(x))
            break
    contador+=1
    if contador==4:
        print("No adivinaste, mi número era "+str(numero))   