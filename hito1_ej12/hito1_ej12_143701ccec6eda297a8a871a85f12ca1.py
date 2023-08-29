#Juego adivina mi número
import random
x = random.randint(1, 20)
i = 1
while i <= 5:
    y = int(input("Haz un intento: "))
    if x == y:
        print("Adivinaste, mi número era ",x)
    if x > y:
        print("Mi numero es mayor")
    if x < y:
        print("Mi numero es menor")
    i += 1
print("No adivinaste, mi numero era: ",x)