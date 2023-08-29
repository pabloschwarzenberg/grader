#Juego adivina mi número
import random
from random import*

na = randint(1,20)

contador = 1
while contador <=5:
    n = int(input("ingrese su numero:"))
    if n > na:
        print("mi numero es menor")
    if n < na:
        print("mi numero es mayor")
    if n == na:
        print("es mi numero")
        contador = 6       
    else:
        print("intente otra vez")
        if contador == 5:
            print("se te acabaron los intentos")
        contador = contador +1
      