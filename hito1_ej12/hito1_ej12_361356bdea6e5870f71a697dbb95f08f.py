import random

numero = random.randint(1,20)
i = 0
b = 5

while i < 5:
    adivina = int(input('Intenta adivinar el numero tienes {} intentos: '.format(b)))
    i = i + 1

    if numero == adivina:
        print('Adivinaste, mi número era {}'.format(numero))
        break
    else:
        b = b - 1
        if numero < adivina:
            print('mi número es menor')
        elif numero > adivina:
            print('mi número es mayor')
            if b == 0:
                print('No adivinaste, mi número era {}'.format(numero))
                break