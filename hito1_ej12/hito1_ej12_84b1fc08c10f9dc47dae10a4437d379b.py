import random

r = random.randint(1, 20)
x = 0
cont = 0

while x != r and cont < 6:
    x = int(input("numero: "))
    if x < r:
        print("mi número es mayor\n")
        cont += 1
        if cont == 5:
            print("No adivinaste, mi número era "+str(r))
            break
    elif x > r:
        print("mi número es menor\n")
        cont += 1
        if cont == 5:
            print("No adivinaste, mi número era "+str(r))
            break
    elif x == r:
        print("Adivinaste, mi número era "+str(r))
        break