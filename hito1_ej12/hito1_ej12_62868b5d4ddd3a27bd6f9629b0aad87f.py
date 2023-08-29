import random

contador = 0
ns = random.randint(1, 20)
n = int(input("adivina el numero:"))

while contador < 5:
    if n == ns:
        print("Adivinaste, mi numero era", ns)
        break
    elif n < ns:
        print("es mayor")
        contador += 1
        n = int(input("adivina el numero:"))

    else:
        print("es menor")
        contador += 1
        n = int(input("adivina el numero:"))

if contador==5:
    print("No adivinaste, mi numero era", ns)


    