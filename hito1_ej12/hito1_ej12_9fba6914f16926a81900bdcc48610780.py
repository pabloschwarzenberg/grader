import random

y = random.randint(10,20)
i = 5
xx = 1
numero = int(input("ingresa un numero: "))

while (numero != y) and (i > 1):
    if(numero>y):
        print("ingresa un menor numero")
    elif (numero < y):
        print("ingresa mayor numero")
    i = i - 1
    xx = xx + 1
    print("Te quedan", numero, "intentos")
    numero = int(input("ingresa un numero: "))

if (numero == y):
    print("Adivinaste, mi numero es", y)
else:
    print("No adivinaste, mi numero era", y)