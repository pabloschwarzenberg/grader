#el juego de adivinar el nuremo
import random

intentosRealizados = 0

y = random.randint(1, 20)

while intentosRealizados < 5:
    print("intenta adivinar.")
    x = int(input())
    
    intentosRealizados = intentosRealizados + 1

    if x > y:
        print("mi número es menor")

    if x < y:
        print("mi número es mayor")

    if x == y:
        break

if x == y:
    print("adivinaste, mi número era" + str(y)) 

if x != y:
    print("no adivinaste, mi número era" + str(y))
