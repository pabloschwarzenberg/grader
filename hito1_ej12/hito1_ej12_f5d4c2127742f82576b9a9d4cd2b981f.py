# Juego adivina mi número
from random import randrange

numeroAzar = randrange(20)
intentos = 5
numero = 0
print(numeroAzar)

while numero != numeroAzar:
    intentos = intentos - 1

    numero = int(input("numero: "))
    if intentos == 0:
        print("No adivinaste, mi numero era", numeroAzar)
        break
    elif numero < numeroAzar:
        print("Mi numero es mayor")
    elif numero > numeroAzar:
        print("Mi numero es menor")
    else:
        print("Adivinaste, mi numero era", numeroAzar)