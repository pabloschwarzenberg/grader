import random

guess = random.randint(1,20)

contador = 1

while contador < 5:
    intento = int(input('Adivina mi número'))
    if intento > guess:
        contador += 1
        print('Mi número es menor')
    elif intento < guess:
        contador += 1
        print('Mi número es mayor')
    elif intento == guess:
        print('Adivinaste, mi número era: ',guess)
        contador = 5

if intento != guess and contador == 5:
    print('No adivinaste, mi número era: ',guess)
    