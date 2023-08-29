#Juego adivina mi número
import random

adivina = random.randint(1, 20)

print("Adivina mi número entre el 1 y 20")
print("Eso si, solo tienes 5 intentos")
num = int(input("Intenta adivinarlo:"))

if num == 12:
   print("Adivinaste, mi número era: 12")
else:
    if num > adivina:
        print("Mi número es menor")
    else:
        print("Mi número es mayor")
    print("Te quedan 4 intentos")
    num = int(input("Intenta otra vez:"))
if num == 12:
   print("Adivinaste, mi número era: 12")
else:
    if num > adivina:
        print("Mi número es menor")
    else:
        print("Mi número es mayor")
    print("Te quedan 3 intentos")
    num = int(input("Intenta otra vez:"))
if num == 12:
   print("Adivinaste, mi número era: 12")
else:
    if num > adivina:
        print("Mi número es menor")
    else:
        print("Mi número es mayor")
    print("Te quedan 2 intentos")
    num = int(input("Intenta otra vez:"))
    if num == 12:
        print("Adivinaste, mi número era: 12")
    else:
        if num > adivina:
            print("Mi número es menor")
        else:
            print("Mi número es mayor")
        print("Te quedan 1 intentos")
        num = int(input("Intenta otra vez:"))
        if num == 12:
            print("Adivinaste, mi número era: 12")
        else:
            print("No adivinaste, mi numero era: 12")

