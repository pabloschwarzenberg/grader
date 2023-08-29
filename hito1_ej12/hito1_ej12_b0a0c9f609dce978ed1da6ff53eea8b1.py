#Juego adivina mi número
import random

numero_secreto = random.randint(1,20)
intentos = 0

while intentos < 5:
    numero = int(input("Ingresa un numero: "))
    if numero < numero_secreto:
        print("Mi número es mayor")
        intentos += 1
    elif numero > numero_secreto:
        print("Mi número es menor")
        intentos += 1
    elif numero == numero_secreto:
        print("Adivinaste, mi número era " + str(numero_secreto))
        intentos = 6
if intentos == 5:
    print("No adivinaste, mi número era " + str(numero_secreto))   