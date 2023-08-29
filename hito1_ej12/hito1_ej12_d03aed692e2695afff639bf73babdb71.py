#Juego adivina mi número
import random
a = random.randint (1, 20)
intentos = 1
while intentos < 6:
    b = int(input("ingresa un numero: "))
    if a == b:
        print("Adivinaste, mi número era",a)
        break
    elif a > b:
        print("mi número es mayor")
    elif a < b:
        print("mi número es menor")
    if intentos > 5:
        print("No adivinaste, mi número era",a)

    intentos += 1 