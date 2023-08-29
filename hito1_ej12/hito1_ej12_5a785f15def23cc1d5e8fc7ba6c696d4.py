#Juego adivina mi número
import random
from random import*

num = randint(1,20)

Intentos = 1
while Intentos <=5:
    n = int(input("ingrese su numero:"))
    if n > num:
        print("mi numero es menor")
    if n < num:
        print("mi numero es mayor")
    if n == num:
        print("es mi numero")
        Intentos = 6
    else:
        print("intente otra vez")
        if Intentos == 5:
            print("se te acabaron los intentos")
        Intentos = Intentos +1