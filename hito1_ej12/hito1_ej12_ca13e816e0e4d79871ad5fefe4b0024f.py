import random
n=random.randint(1,20)
i=0
print('- tienes 5 intentos para adivinar el número secreto')
while i<5:
    j=int(input('>>> ingresa el número que piensas que es: '))
    if j<n:
        print('cerca, pero el número que ingresaste es MENOR al número secreto')
        i+=1
    elif j>n:
        print('cerca, pero el número que ingresaste es MAYOR al número secreto')
        i+=1
    elif j==n:
        print('¡ADIVINASTE!, felicitaciones mi número era', n)
else:    
    print('¡Mala suerte! no adivinaste, mi número era ',n)