#Juego adivina mi número
import random as rnd
a = rnd.randrange(20)
i = 0
while i < 5:
    x = int(input("Ingrese el numero: "))
    if x < a:
        print("Mi numero es mayor")
    if x > a:
        print("Mi numero es menor")
    i += 1
    if x == a:
        print("Adivinaste, mi numero era:" + str(a))
        break
else:
    print("No adivinaste, mi numero era:" + str(a))