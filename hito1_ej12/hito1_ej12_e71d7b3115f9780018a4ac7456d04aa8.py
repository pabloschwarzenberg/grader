#Juego adivina mi número
import random
numero = random.randint(0,20)

adivina = int(input("Ingresa un número: "))

intentos = 1
while numero != adivina:
    if intentos == 5:
        print("No adivinaste, mi número era", numero)
        break
    else:
        intentos = intentos + 1
        if numero > adivina:
            print("El numero secreto es mayor")
            adivina = int(input("Ingresa un número: "))
        elif numero < adivina:
            print("El numero secreto es menor")
            adicina = int(input("Ingresa un número: "))
        
if numero == adivina:
    print("Adivinaste, mi número era", numero)      