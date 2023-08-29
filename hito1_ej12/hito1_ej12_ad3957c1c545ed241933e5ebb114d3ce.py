#Juego adivina mi número
import random

ranmin = 1
ranmax = 20
blnadiv = False
intentos = 5
numRandom = random.randint(ranmin , ranmax)

for i in range(5):
    num = int(input("Ingrese numero: "))
    if num == numRandom and intentos != 0:
        print('Adivinaste, mi numero era')
        print(numRandom)
        #blnadiv = True
        #break
    elif num < numRandom:
        intentos -= 1
        print("El numero es mayor")
    elif  num > numRandom:
        intentos -= 1
        print("El numero es menor")       
    if intentos == 0:
        print("No adivinaste, mi numero era", numRandom)