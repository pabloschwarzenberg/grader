#Juego adivina mi número

import random

intentos=0

N=random.randint(1,20)
print('algun numero entre 1 y 20.')
while intentos<5:
    adivina=input()
    adivina=int(adivina)
    intentos=intentos+1
    if adivina<N:
        print ('mi número es mayor')
    if adivina>N:
        print('mi número es menor')
    if adivina==N:
        break
if adivina==N:
    print('Adivinaste, mi número era '+ str(N))
if adivina!=N:
    print("No adivinaste, mi número era "+ str(N))