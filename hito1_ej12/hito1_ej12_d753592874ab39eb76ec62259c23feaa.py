#Juego adivina mi número

import random

Mi_numero=random.randint(1,20)
print(Mi_numero)


intentos=5
while intentos>0:
    numero_jugador=int(input("Adivina mi número: "))
    if numero_jugador<Mi_numero:
        print("mi numero es mayor")
        intentos-=1
    elif numero_jugador>Mi_numero:
        print("mi numero es menor")
        intentos-=1
    else:
        print("Adivinaste, mi número era {0} ".format(Mi_numero))
        break
if intentos==0:
    print("No adivinaste, mi número era {0} ".format(Mi_numero))
