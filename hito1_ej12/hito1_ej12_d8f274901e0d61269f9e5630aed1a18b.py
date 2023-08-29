#Juego adivina mi número
#random.randint
#while <5
#int(random.randint)

#Import the techniques
import random
intentos = 0
#Generar random
a=1
b=20
x = random.randint(a,b)
#Progamacion de while
while intentos < 5:
    y = int(input("Adivina un numero del 1 al 20: "))
#Adivina el número
    if y == int(x):
        print("Adivinaste, mi número era",x)
#No adivina el número
    else:
        intentos = intentos + 1
        if y >= int(x):
            print("mi número es menor")
        if y <= int(x):
            print("mi número es mayor")
        if intentos == 5:
            print("No adivinaste, mi número era",x)