#Juego adivina mi número
import random

secreto = random.randint(1, 20)
print("He elegido un número entre 1 y 20. Tienes 5 intentos para adivinar mi número.")

for intento in range(1, 6):
    print("Intento " + str(intento) + ": ")
    guess = int(input())

    if guess < secreto:
        print("Mi número es mayor.")
    elif guess > secreto:
        print("Mi número es menor.")
    else:
        break

if guess == secreto:
    print("¡Adivinaste! Mi número era " + str(secreto))
else:
    print("No adivinaste. Mi número era " + str(secreto))
