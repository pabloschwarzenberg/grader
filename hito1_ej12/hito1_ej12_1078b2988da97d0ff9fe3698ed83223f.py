#Juego adivina mi número

import random

n = random.randint(1, 20)
intentos = 0
t = True

while t:
    guess = int(input("Ingrese numero: "))
    if guess == n:
        print("Adivinaste, mi numero era",n)
        t = False
    else:
        if intentos == 4:
            print("No adivinaste, mi numero era", n)
            t = False
        
        elif guess > n:
            print("Mi numero es menor")
            intentos +=1
        else:
            print("Mi numero es mayor")
            intentos +=1
        
        
