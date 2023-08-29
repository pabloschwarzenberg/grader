#Juego adivina mi número
from random import randint
numero = randint(1, 20)
adivinaste = False
intentos = 0

while intentos < 5 and adivinaste == False:
    n = input("Adivina un número entre el 1 y el 20: ")
    if n.isdigit():
        n = int(n)
        if n == numero:
            print("Adivinaste, mi número era " + str(numero))
            adivinaste = True
        elif n < numero:
            print("mi número es mayor")
        elif n > numero:
            print("mi número es menor")
    intentos += 1

if adivinaste == False:
    print("No adivinaste, mi número era " + str(numero))      