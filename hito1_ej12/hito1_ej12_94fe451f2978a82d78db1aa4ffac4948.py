#Juego adivina mi número
import random
a = 0
n = random.randint(1, 20)

while a<5:

    ni = int(input('\nIngrese un número: '))

    if ni>n:
        print('\nMi número secreto es menor.')
    elif ni<n:
        print('\nMi número secreto es mayor.')
    elif ni==n:
        print('\nAdivinaste, mi número era ', n)
        break
    
    a = a+1

if a==5:
    print('\nNo adivinaste, mi número era ', n)