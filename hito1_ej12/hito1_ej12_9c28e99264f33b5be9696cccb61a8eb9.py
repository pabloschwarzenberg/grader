#Juego adivina mi número
import random
numero = random.randint(1, 20)
n = int(input("ingresa un numero entre 1 y 20: "))
i = 0
while i <= 5:
    if n < numero:
        print("mi numero es mayor")
    elif n > numero:
        print("mi numero es menor")
    elif n == numero:
        print("Adivinaste, mi número era", numero)
        i = 6
    else:
        print("No adivinaste, mi número era ", numero)
    i += 1