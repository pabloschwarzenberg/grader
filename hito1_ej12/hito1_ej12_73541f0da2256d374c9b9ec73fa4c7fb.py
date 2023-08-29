import random

numero_secreto = random.randint(1, 20)
intentos = 5

while intentos > 0:
    print("Intentos restantes: ",intentos)
    numero = int(input("Ingresa un número: "))

    if numero == numero_secreto:
        print("Adivinaste, mi número era ",numero_secreto)
        break
    elif numero < numero_secreto:
        print("Mi número es mayor.")
    else:
        print("Mi número es menor.")

    intentos -= 1

if intentos == 0:
    print("No adivinaste, mi número era ",numero_secreto)

      