import random

numero_secreto = random.randint(1, 20)
intentos = 5

print("¡Bienvenido al juego Adivina mi número!")
print("Tienes 5 intentos para adivinar un número entre 1 y 20.")

for i in range(intentos):
    numero = int(input("Ingresa tu número: "))

    if numero == numero_secreto:
        print("¡Adivinaste! Mi número era", numero_secreto)
        break
    elif numero < numero_secreto:
        print("Mi número es mayor")
    else:
        print("Mi número es menor")

if numero != numero_secreto:
    print("No adivinaste. Mi número era", numero_secreto)