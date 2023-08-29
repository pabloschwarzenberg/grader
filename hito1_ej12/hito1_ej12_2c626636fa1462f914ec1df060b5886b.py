from random import randint, uniform, random

j = randint(0, 20)
i = 0
while i < 6:
    x = int(input("Adivina el numero"))
    if x > j:
        print("Mi numero es menor")
    elif x < j:
        print("Mi numero es mayor")
    elif x == j:
        print("Adivinaste, mi numero era:", j)
        break
    i += 1
else:
    print("No adivinaste, el numero era", j)