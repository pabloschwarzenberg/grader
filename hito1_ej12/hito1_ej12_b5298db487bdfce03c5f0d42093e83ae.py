#Juego adivina mi número
from random import  randint

numero_secreto = randint(1,20)
intentos = 5


while intentos > 0:
    numero = int(input("Mi número es?: "))
    if numero == numero_secreto:
        print("Adivinaste, mi número era", numero_secreto)
        break
    elif numero != numero_secreto and numero > numero_secreto:
        print("mi número es menor")
        intentos = intentos - 1
    elif numero != numero_secreto and numero < numero_secreto:
        print("mi número es mayor")
        intentos = intentos - 1
if intentos == 0:
    print("No adivinaste, mi número era ", numero_secreto)
