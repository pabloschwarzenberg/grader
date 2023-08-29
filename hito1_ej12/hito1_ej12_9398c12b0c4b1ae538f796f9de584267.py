#Juego adivina mi número
import random
juego=random.randint(1,20)
jugador= int(input())
for i in range(5):
    if juego==jugador:
        print ("Adivinaste, mi número era",juego)
    else:
        if i<5 and juego>jugador:
            print("el numero secreto es mayor")
        if i<5 and juego<jugador:
            print("el numero secreto es menor")
        if i>=5 and juego!=jugador:
            print ("NO adivinaste, mi número era",juego)
        