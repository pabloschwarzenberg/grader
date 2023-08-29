#Juego adivina mi número
import random

numero_secreto = random.randint(1, 20)
intentos = 0

while intentos < 5:
    numero = int(input("Ingresa un número entre 1 y 20: "))
    intentos += 1
    
    if numero == numero_secreto:
        print("Adivinaste, mi número era", numero_secreto)
        break
    elif numero < numero_secreto:
        print("Mi número es mayor")
    else:
        print("Mi número es menor")

if intentos == 5:
    print("No adivinaste, mi número era", numero_secreto)
