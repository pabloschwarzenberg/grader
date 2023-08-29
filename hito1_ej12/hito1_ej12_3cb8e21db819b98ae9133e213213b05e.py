#Juego adivina mi número
import random

numero_secreto = random.randint(1, 20)

intentos = 0
while intentos < 5:
    num1 = int(input('Ingresa un número para adivinar el número secreto: '))
    
    if num1 == numero_secreto:
        print('Adivinaste, mi número era', numero_secreto)
        break
    elif num1 < numero_secreto:
        print("Mi número es mayor.")
    else:
        print("Mi número es menor.")
    
    intentos += 1

if intentos == 5:
    print("No adivinaste, mi número era", numero_secreto)
      