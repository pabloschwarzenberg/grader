#Juego adivina mi número
import random
n=random.randint(1,20)
T=0
print('- tienes 5 intentos para adivinar el número secreto')
while T<5:
    E=int(input('>>> ingresa el número que piensas que es: '))
    if E<n:
        print('cerca, pero el número que ingresaste es MENOR al número secreto')
        T+=1
    elif E>n:
        print('cerca, pero el número que ingresaste es MAYOR al número secreto')
        T+=1
    elif E==n:
        print('¡ADIVINASTE!, felicitaciones mi número era',n)
else:    
    print('¡Mala suerte! no adivinaste, mi número era ',n)    