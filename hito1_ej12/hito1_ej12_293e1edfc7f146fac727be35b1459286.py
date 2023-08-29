#Juego adivina mi número
import random
numero_secreto = random.randint(1, 20)
vidas = 5
jugando = True

while(jugando and vidas != 0):
    num = int(input("> "))
    if num < numero_secreto:
        print("El numero secreto es mayor")
        vidas -= 1
    elif num > numero_secreto:
        print("El numero secreto es menor")
        vidas -= 1
    elif num == numero_secreto:
        jugando = False

if vidas != 0:
    print("Adivinaste, mi número era",numero_secreto)
else:
    print("No adivinaste, mi número era",numero_secreto)