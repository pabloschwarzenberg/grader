#Juego adivina mi número
import random

numero_secreto = random.randint(1, 20)
intentos = 5

while intentos > 0:
    adivinanza = int(input())
    if adivinanza == numero_secreto:
        print("Adivinaste, mi número era", numero_secreto)
        break
    elif adivinanza < numero_secreto:
        print("Mi número es mayor.")
    else:
        print("Mi número es menor.")
    adivinanza -= 1

if adivinanza == 0:
    print("No adivinaste. Mi número era", numero_secreto)