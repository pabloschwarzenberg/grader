#Juego adivina mi número
import random
adivinar = random.randint(1, 20)
intentos = 5

while intentos > 0:
    numero = int(input("Adivina mi número (entre 1 y 20): "))
    if numero == adivinar:
        print("Adivinaste, mi número era ", adivinar)
        break
    elif numero < adivinar:
        print("Mi número es mayor")
    elif numero > adivinar:
        print("Mi número es menor")

    intentos-=1
    if intentos == 0:
        print("No adivinaste, mi número era ", adivinar)