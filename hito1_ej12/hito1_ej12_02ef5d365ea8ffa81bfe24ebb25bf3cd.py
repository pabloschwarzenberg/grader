import random

numero = random.randint(1, 20)
intentos = 5

while True:
    num_input = int(input("Ingresa un numero: "))

    if num_input > numero:
        print("Tu numero es mayor.")
    elif num_input < numero:
        print("Tu numero es menor.")
    else:
        print("Adivinaste, el numero era", numero)
        break

    if intentos == 0:
        print("No adivinaste, el numero era", numero)
        break