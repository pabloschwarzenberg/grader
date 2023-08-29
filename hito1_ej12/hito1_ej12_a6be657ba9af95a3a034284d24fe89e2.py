import random

numero_secreto = random.randint(1, 20)
intentos = 5

for i in range(intentos):
    guess = int(input("Adivina mi número: "))
    if guess < numero_secreto:
        print("Mi número es mayor")
    elif guess > numero_secreto:
        print("Mi número es menor")
    else:
        print("Adivinaste, mi número era", numero_secreto)
        break
else:
    print("No adivinaste, mi número era", numero_secreto)
