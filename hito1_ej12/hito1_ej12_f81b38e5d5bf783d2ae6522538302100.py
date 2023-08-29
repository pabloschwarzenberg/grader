#Juego adivina mi número
from random import randint

numero_secreto = randint(1, 20)
intentos = 0
while intentos < 5:
    a = int(input("Ingrese un numero entre 1 y 20: "))
    if 1 <= a <= 20:
        if a == numero_secreto:
            print("Adivinaste, mi numero era {0}".format(numero_secreto))
            break
        elif a < numero_secreto:
            print("Es mayor")
            intentos += 1
        elif a > numero_secreto:
            print("Es menor")
            intentos += 1
    else:
        print("ese no es un numero permitido")

if intentos>5:
    print("No adivinaste, mi numero era {0}".format(numero_secreto))