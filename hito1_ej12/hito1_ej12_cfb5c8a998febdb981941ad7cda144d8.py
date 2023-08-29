#Juego Adivina mi número
import random
n = range(1,21)
numero = random.choice(n)
i=0
while i<5:
    x = int(input("Ingrese un numero:"))
    if x>numero:
        print("mayor")
    elif x<numero:
        print("menor")
    elif x == numero:
        break
    i = i + 1
if x == numero:
    print("Adivinaste, mi número era",numero)
else:
    print("No adivinaste, mi número era",numero)