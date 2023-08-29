#Juego adivina mi número
import random
i = 1
j = 20
ran = random.randint(i,j)
contador = 1
while contador <= 5 :
    num = int(input("Ingresa tu numero: "))
    if num > ran or num < ran:
        if num > ran:
            print("No haz adivinado, mi numero es menor")
            contador += 1
        elif num < ran:
            print("No haz adivinado mi numero es mayor")
            contador += 1
    elif num == ran:
        print("Adivinaste, mi numero era ", ran)
        break
print("No adivinaste, mi numero era: ",ran)