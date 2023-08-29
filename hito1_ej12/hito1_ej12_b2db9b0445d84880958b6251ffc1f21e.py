import random
intentosRealizados = 0
número = random.randint(1, 20)
print('Estoy pensando en un número entre 1 y 20.')
while intentosRealizados < 6:
print('Intenta adivinar.')
estimación = input()
estimación = int(estimación)
intentosRealizados = intentosRealizados + 1
if estimación < número:
print("mi número es mayor")
if estimación > número:
print("mi número es menor")
if estimación == número:
break
if estimación == número:
intentosRealizados = str(intentosRealizados)
print("Adivinaste, mi número era "  + intentosRealizados + )
if estimación != número:
número = str(número)
print("No adivinaste, mi número era "  + número)