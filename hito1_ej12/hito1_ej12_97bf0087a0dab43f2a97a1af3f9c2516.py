#Juego adivina mi número
import random

numero_secreto = random.randint(1, 20)
intentos = 5

print("Bienvenido al juego Adivina mi número. Tienes 5 intentos para adivinar.")

while intentos > 0:
    numero_ingresado = int(input("Ingresa un número entre 1 y 20: "))
    
    if numero_ingresado == numero_secreto:
        print("¡Adivinaste! Mi número era", numero_secreto)
        break
    elif numero_ingresado < numero_secreto:
        print("Mi número es mayor.")
    else:
        print("Mi número es menor.")
    
    intentos -= 1
    if intentos > 0:
        print("Tienes", intentos, "intentos restantes.")
    else:
        print("No adivinaste. Mi número era", numero_secreto)