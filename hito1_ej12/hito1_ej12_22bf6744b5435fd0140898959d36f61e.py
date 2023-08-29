import random

NumeroSecreto=random.randint(1,20)

intentos=0

while intentos<5:
    x=int(input("Cual crees que es mi numero?: "))
    if x<NumeroSecreto:
        print("mi numero es mayor")
    elif x>NumeroSecreto:
        print("mi numero es menor")
    else:
        print("Adivinaste, mi numero era",NumeroSecreto)
        break
    intentos=intentos+1

if intentos==5:
    print("No adivinaste, mi numero era",NumeroSecreto)
