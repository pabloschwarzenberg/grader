#Juego adivina mi número

from random import randint

intentos = 5
numero_misterioso = randint(1, 20)

while intentos > 0:    
    numero = int(input())

    if numero > numero_misterioso:
        print("mi número es menor")
        intentos -= 1
    elif numero == numero_misterioso:
        print("Adivinaste, mi número era {}".format(numero_misterioso))
        break
    else:
        print("mi número es mayor")
        intentos -= 1

if intentos == 0:
    print("No adivinaste, mi número era {}".format(numero_misterioso))
else:
    pass
