#Juego adivina mi número
import random

num = random.randint(1,20)

x = '12345'
for i in x:
    guess=int(input('MakeAGuess: '))
    if num<guess:
        print('mi número es menor')
    if num>guess:
        print('mi número es mayor')
    if num==guess:
        print('Adivinaste. mi número era',num)
        break
if num!=guess:    
 print('No adivinaste, mi número era',num)   
 