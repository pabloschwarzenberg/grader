from random import randint
numSecreto = randint(1,20)
intentos = 0
numUsuario = int(input("ingrese numero de 1 a 20: "))

while numSecreto != numUsuario:
    if numUsuario > numSecreto:
        print("mi numero es menor")
    else:
        print("mi numero es mayor")
    intentos = intentos +1
    if intentos == 5:
        print("No adivinaste, mi número era",numSecreto)
        break
if numSecreto == numUsuario:
    print("adivinaste el numero secreto", numSecreto)


