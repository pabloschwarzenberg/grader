#Juego adivina mi número
import random
numero_secreto = random.randint(1, 20)
intentos = 5
print("tienes 5 intentos para adivinar el número en el cual estoy pensando.")
while intentos > 0:
    print("Intento #", 6 - intentos)
    numero = int(input("Ingresa un número: "))
    if numero < numero_secreto:
        print("Mi número es mayor.")
    elif numero > numero_secreto:
        print("Mi número es menor.")
    else:
        print("Adivinaste, mi número era", numero_secreto,)
        break
    intentos -= 1
if intentos == 0:
    print("No adivinaste, mi número era", numero_secreto,)      