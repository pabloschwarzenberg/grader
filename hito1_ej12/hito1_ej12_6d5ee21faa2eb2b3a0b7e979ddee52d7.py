#Juego adivina mi número
import random

nrandom = random.randint(1,20)
intentos = 5
fin = 1
while fin == 1:

    if intentos == 0:
        print("No adivinaste,mi numero era",nrandom)
        fin = 0
    else:
        numero = int(input("Ingrese un numero :"))
        if numero < nrandom:
            print("Mi numero es mayor")
        else:
            print("Mi numero es menor")
        if numero == nrandom:
            print("Adivinaste, mi numero era",nrandom)
            fin = 0
        intentos = intentos - 1      