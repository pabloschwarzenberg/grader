#Juego adivina mi número
import random
n=random.randint(1,20)
i=0
print('tienes 5 intentos para adivinar mi numero')
while i<5:
    jugador=int(input('>>>> ingresa un numero: '))
    if jugador<n:
        print('el numero que ingresaste es menor al numero secreto')
        i+=1
    elif jugador>n:
        print('el numero que ingresaste es mayor al numero secreto')
        i+=1
    elif jugador==n:
        print('¡ADIVINASTE!, felicitaciones mi número era', n)
else:    
    print('¡Mala suerte! no adivinaste, mi número era ',n)      