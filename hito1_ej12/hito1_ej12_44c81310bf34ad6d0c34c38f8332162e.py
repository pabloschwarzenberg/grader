#Juego adivina mi número
import random
intentos = 1
num = random.randint(1, 20)


while intentos <= 5 :
    x=int(input('adivina mi numero del 1 al 20:'))
    print(' ')
    intentos = intentos + 1

    if x > num:
        print('mi numero es menor')
        print(' ')

    if x < num:
        print('mi numero es mayor')
        print(' ')

    if x == num:
        break

if x == num:
    print('adivinaste, mi numero era',num)

if x!= num:
    print('no adivinaste, mi numero era',num)      