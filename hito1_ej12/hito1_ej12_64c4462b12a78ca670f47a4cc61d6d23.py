#Juego adivina mi número

from random import randint

hidden_number = randint(1,20)
attempts = 5
while attempts > 0:
    n = int(input('Adivina: '))
    if n == hidden_number:
        print('Adivinaste, mi número era', hidden_number)
        break
    elif n > hidden_number:
        print('Tu número es mayor al mío')
        attempts -= 1
    else:
        print('Tu número es menor al mío')
        attempts -= 1
if attempts == 0:
    print('No adivinaste, mi número era', hidden_number)
