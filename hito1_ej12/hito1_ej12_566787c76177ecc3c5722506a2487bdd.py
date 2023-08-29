#Juego adivina mi número
import random 
NA=random.randint(1,20)
intentos=0
while intentos<5:
    I=int(input('ingrese su numero'))
    if I==NA:
        print('Adivinaste, mi numero era: ',NA)
        break 
    elif I<NA:
        print('tu numero es menor')
    elif I>NA:
        print('tu numero es mayor')
    intentos=intentos+1


if NA!=I:
    print('No adivinaste, mi numero era: ',NA)
    
      