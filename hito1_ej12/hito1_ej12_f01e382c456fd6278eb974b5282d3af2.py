#Juego adivina mi número
from random import randint

numero = randint(1,20)
intentos = 5
ganador = False
i=1
while i <= intentos:
    n = eval(input("intento {}: ".format(i)))
    if n == numero:
        ganador = True
        break
    elif n < numero:
        print("Mi número es menor")
    else:
        print("Mi número es mayor")
    i += 1


if ganador: print("Adivinaste, mi número era ",numero)
else: print("No adivinaste, mi número era ",numero)