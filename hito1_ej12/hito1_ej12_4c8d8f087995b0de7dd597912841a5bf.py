import random

numero_secreto = random.randint(1, 20)
intentos = 5

for i in range(intentos):
    numero_jugador = int(input("Adivina mi número: "))
    if numero_jugador == numero_secreto:
        print("Adivinaste, mi número era", numero_secreto)
        break
    elif numero_jugador < numero_secreto:
        print("Mi número es mayor")
    else:
        print("Mi número es menor")
else:
    print("No adivinaste, mi número era", numero_secreto)