from random import randint
nr = randint(1,20)
i = 0
while i < 5:
    perdiste = True
    n = int(input("Ingresa el numero: "))
    if n > nr:
        print("Mi numero es mayor")
        i += 1
    elif n < nr:
        print("Mi numero es menor")
        i += 1
    elif n == nr:
        print("Adivinaste, mi numero era ", nr)
        perdiste = False
        break
if perdiste:
    print("No adivinaste, mi numero era ", nr)