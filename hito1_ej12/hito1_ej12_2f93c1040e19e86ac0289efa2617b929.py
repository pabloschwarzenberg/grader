#Juego adivina mi número
from random import randrange
num = randrange(1,21)
cont = 0
while cont < 5:
    x = int(input("ingrese un numero: "))
    if x == num:
        print("Adivinaste, mi numero era {}".format(num))
        cont = 5
    elif x > num:
        print("mi numero es menor")
    elif x < num:
        print("mi numero es mayor")
    cont += 1
if num != x:
    print("No adivinaste, mi numero era {}".format(num))   