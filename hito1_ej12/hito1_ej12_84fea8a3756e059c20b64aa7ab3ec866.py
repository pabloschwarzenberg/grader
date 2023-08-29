#Juego adivina mi número

import random
secreto = random.randrange(1,20)
x = int(input("Ingrese un numero entre 1 y 20: "))
intentos = 1

while (x != secreto) or (intentos <= 4):
    if x < 1 or x > 20:
        print("Ese no es un numero valido")
        x = int(input())
        intentos = intentos + 1
        
    if x < secreto:
        print("mi número es mayor")
        x = int(input())
        intentos = intentos + 1
        
    if x > secreto:
        print("mi número es menor")
        x = int(input())
        intentos = intentos + 1
        
    if (x == secreto):
        print("Adivinaste, mi número era ",secreto)
        break
        
    if (intentos > 4):
        print("No adivinaste, mi número era ",secreto)
        break

else:
    print("ERROR")
    input()