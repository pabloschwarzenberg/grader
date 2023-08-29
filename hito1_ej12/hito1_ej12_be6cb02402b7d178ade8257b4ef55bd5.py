#Juego adivina mi número
import random

numero = random.randint(1, 20)
intentos = 0
numero_secreto = 0

while intentos <= 5:
    if intentos > 1:
        numero_secreto = int(input("Ingresa el numero para adivinar: "))
    else:
        numero_secreto = int(input("Ingresa el numero para adivinar: "))
        
    intentos = intentos + 1
    if numero_secreto == numero:
        print("Adivinaste, mi número era: ",numero)
        break
    if numero > numero_secreto:
        print("Mi numero es mayor")
    else:
        print("Mi numero es menor")
    if intentos == 5:
        print("No adivinaste, mi numero era: ",numero)
        break