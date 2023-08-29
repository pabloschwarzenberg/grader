#Juego adivina mi número
import random

numRandom = random.randint(1,20)
print(numRandom)
ctdadIntentos = 0


while ctdadIntentos < 5:
    miNumero = int(input("ingrese un numero entre 1 y 20: "))

    if miNumero != numRandom:
        if miNumero > numRandom:
            print("mi número es menor")
        elif miNumero < numRandom:
            print("mi número es mayor")
        ctdadIntentos = ctdadIntentos + 1
    elif miNumero == numRandom:
        print("Adivinaste, mi número era ", numRandom)
        break

if ctdadIntentos == 5:
    print("No adivinaste, mi número era ", numRandom)

    