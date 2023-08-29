#Juego adivina mi número
import random
numSecreto = random.randint(1,20)
num = int(input("Adivina el número secreto: "))
intentos = 1

while num !=  numSecreto and intentos <= 5:
    if num < numSecreto:
        print("Mi número es mayor")
        num = int(input("Adivina el número secreto: "))
        intentos += 1
    elif num > numSecreto:
        print("Mi número es menor")
        num = int(input("Adivina el número secreto: "))
        intentos +=1

if num == numSecreto:
    print("Adivinaste, mi número era "  + str(numSecreto))
elif intentos > 5:
    print("No adivinaste, mi número era" + str(numSecreto))
              