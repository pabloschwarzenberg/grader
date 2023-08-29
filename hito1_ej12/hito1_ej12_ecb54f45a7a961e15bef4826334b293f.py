#Juego adivina mi número
import random
juegos=5
numero=random.randint(1,20)
while juegos>0:
    a=int(input())
    if a<numero:
        print("mi numero es mayor")
    elif a>numero:
        print("mi numero es menor")
    juegos=juegos-1
    if a==numero:
        print("Adivinaste, mi numero era",numero)
    elif juegos==0:
        print("No adivinaste, mi numero era",numero)