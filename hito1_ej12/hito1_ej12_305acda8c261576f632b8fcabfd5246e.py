#Juego adivina mi número
import random
a=random.randint(1,20)
b=0
print('tienes 5 intentos para adivinar el número secreto')
while b<5:
    j=int(input('ingresa el número: '))
    if j<a:
        print('por poco, pero el número que ingresaste es MENOR al número secreto')
        b+=1
    elif j>a:
        print('por poco, pero el número que ingresaste es MAYOR al número secreto')
        b+=1
    elif j==a:
        print('¡felicitaciones!, mi número era', a)
else:    
    print('¡no adivinaste!, mi número era ',a)