#Juego adivina mi número
from random import randint
nRand=(randint(1,20))
intento=0
print(nRand)
while intento<5:
    Letra = int(input("Ingrese un numero: "))
    if Letra == nRand:
        print("Adivinaste, mi número era: ",nRand)
        intento=intento+6
    elif Letra > nRand:
        print("mi número es menor")
        intento = intento + 1
        if intento == 5:
            print("No Adivinaste, mi número era: ", nRand)
    elif Letra < nRand:
        print("mi número es mayor:")
        intento = intento + 1
        if intento == 5:
            print("No adivinaste, mi número era: ", nRand)
