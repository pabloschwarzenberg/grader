#Juego adivina mi número
import random
ints = 0
num=random.randint(1,20)
print('Piensa un número entre 1 y 20.')
while ints<5:
    adv=input()
    adv=int(adv)
    ints=ints+1
    if adv<num:
        print ('mi número es mayor')
    if adv>num:
        print('mi número es menor')
    if adv==num:
        break
if adv==num:
    print('Adivinaste, mi número era '+ str(num))
if adv!=num:
    print("No adivinaste, mi número era "+ str(num))