from random import randint
i=0
numero=randint(1,20)

while i<=5:
    jugador=input('adivina mi número: ')
    jugador=int(jugador)
    if jugador<numero:
        print('Mi numero es mayor')
        i=i+1
    if jugador>numero:
        print('Mi numero es menor')
        i=i+1
    if jugador==numero:
        print('Adivinaste, mi número era',numero)
        break
if i>5:
    print('No adivinaste, mi número era',numero)

