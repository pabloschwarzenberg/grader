import random

numero_random = random.randint(1,20)

adivino = False
for i in range(5):
    numero = int(input("Ingrese un número: "))
    if(numero == numero_random):
        print("Adivinaste, mi número era %d" %numero)
        adivino = True
        break
    if(numero > numero_random):
        print("mayor")
    else:
        print("menor")

if(not adivino):
    print("No adivinaste, mi número era %d" %numero_random)
      