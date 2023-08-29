import random

numero_secreto = random.randint(1, 20)
intentos = 5

while intentos > 0:
    intentos -= 1
    adivinanza = int(input("Adivina mi numero: "))

    if adivinanza == numero_secreto:
        print("Adivinaste, mi numero era", numero_secreto)
        break
    elif adivinanza < numero_secreto:
        print("Mi numero es mayor")
    else:
        print("Mi numero es menor")

if intentos == 0:
    print("No adivinaste, mi numero era", numero_secreto)
