#Juego adivina mi número
from random import randrange
rand = randrange(1,20)
x = 0
while x < 5:
    number = int(input("Ingrese un numero entre 1 y 20: "))
    if(number >=1 and number <= 20):
        if(number > rand):
            print("Mi numero es mayor")
        if(number < rand):
            print("Mi numero es menor")
        if(number == rand):
            print("Adivinaste, mi número era",rand)
            break
    x = x + 1