import random
real = random.randint(1,20)
intentos = 0
print(real)
jugando = True

while jugando:
    intentos += 1
    if intentos <=5:
        num=int(input('Adivina el número entre 1 y 20: '))
        if num == real:
            print('Adivinaste, mi número era',real)
            jugando = False
        elif num > real:
            print('Mi número es menor')
        elif num < real:
            print('Mi número es mayor')
    else:
        print('No adivinaste, mi número era',real)
        jugando=False