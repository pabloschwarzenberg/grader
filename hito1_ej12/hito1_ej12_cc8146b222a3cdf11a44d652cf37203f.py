import random

numero_random = random.randint(1, 20)   # 18
intentos = 0

numero = 1000
while numero != numero_random:

    numero = int(input("Ingresa un valor: "))

    if numero > numero_random:
        print("Mi número es menor")
        intentos = intentos + 1
        if intentos == 5:
            print("No adivinaste, mi numero era", numero_random)
            numero = numero_random

    elif numero < numero_random:
        print("Mi número es mayor")
        intentos = intentos + 1
        if intentos == 5:
            print("No adivinaste, mi numero era", numero_random)
            numero = numero_random

    elif numero == numero_random:
        print("Adivinaste, mi número era", numero_random)
        numero = numero_random