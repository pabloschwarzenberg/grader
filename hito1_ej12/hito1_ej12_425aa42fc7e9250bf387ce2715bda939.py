#Juego adivina mi número
import random
numganador=random.randint(1,20)
numintentos = 0
print("este juego consta de adivinar un número del 1 al 20 con 5 intentos")
while numintentos <=5:
    numintentos+=1
    if numintentos <=5:
        num=int(input("elija un número: "))
        if num == numganador:
            print("Adivinaste, mi número era",numganador)
            numintentos+=10
        elif num > numganador:
            print("mi número es menor, te quedan",numintentos,"de 5 intentos")
        elif num < numganador:
            print("mi número es mayor, te quedan",numintentos,"de 5 intentos")
if num != numganador:
    print("No adivinaste, mi número era", numganador)