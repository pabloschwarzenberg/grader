#Juego adivina mi número
import random
numero_secreto = random.randint(1, 20)
intentos = 0
while intentos < 5:
    numero_ingresado = int(input("Ingresa un número entre 1 y 20: "))
    intentos += 1
    if numero_ingresado == numero_secreto:
        print("¡Adivinaste! Mi número era", numero_secreto)
        break
    elif numero_ingresado < numero_secreto:
        print("Mi número es mayor")
    else:
        print("Mi número es menor")
if intentos == 5:
    print("No adivinaste, mi número era", numero_secreto)
