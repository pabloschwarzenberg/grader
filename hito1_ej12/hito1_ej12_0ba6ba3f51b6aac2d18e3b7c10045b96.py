#Juego adivina mi número
import random
a=random.randint(1,20)
b=1
while (b!=6):
    j=int(input('Ingrese numero:'))
    if a>j:
        print('numero menos, intenta otra vez:')
        b+=1        
    elif a<j:
        print('numero mayor, intenta otra vez:')
        b+=1
    elif a==j:
        print('Adivinaste!, mi numero era',a)
        break
    else:
        print('No adivinaste, mi numero era',a)
        break



      