from random import randint
numerosecreto = randint(1, 20)
intentos=5
while intentos>=0:
    n=int(input('Ingrese numero: '))
    if n==numerosecreto:
        print('Adivinaste el numero era',numerosecreto)
        break
    if n<numerosecreto:
        print('mi numero es mayor')
    if n>numerosecreto:
        print('mi numero es menor')
    intentos=intentos-1
    if intentos==0:
        print("No adivinaste, mi número era ", numerosecreto)
     
        
