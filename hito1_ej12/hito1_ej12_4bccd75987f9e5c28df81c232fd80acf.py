from random import randint


i = 0
numeroaleatorio = randint(1,20)

while i < 5:
    i += 1
    n = eval(input("Ingrese el número: "))
    if n == numeroaleatorio:
        print("Adivinaste, mi numero era ",numeroaleatorio)
        break
    elif n < numeroaleatorio:
        print("mi número es mayor")
    elif n > numeroaleatorio:
        print("mi número es menor")

if n != numeroaleatorio:
    print("No adivinaste, mi numero era ",numeroaleatorio)