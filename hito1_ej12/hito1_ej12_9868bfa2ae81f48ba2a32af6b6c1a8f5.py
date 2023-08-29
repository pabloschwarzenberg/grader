#Juego adivina mi número
import random
x = random.randint(1,20)
i = 0
while i < 5:
    n = int(input("Ingrese el numero: "))
    if n > x:
        print("Mi numero es menor")
    if n < x:
        print("Mi numero es mayor")
    if n == x:
        print("Adivinaste, mi numero era ",x)
        break
    i+=1
    if i == 5:
        print("No adivinaste, mi numero era ",x)      