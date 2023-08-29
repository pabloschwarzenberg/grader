import random
i=0
numero=random.randint(1,20)
while i<5:
    usuario=int(input('Ingrese numero:'))
    if numero<usuario:
        i+=1
        if i==5:
            print('No adivinaste, mi numero era:', numero)
        else:
            print('El numero es menor al que ingresaste')
    elif numero>usuario:
        i+=1
        if i==5:
            print('No adivinaste, mi numero era:',numero)
        else:
            print('El numero es mayor al que ingresaste')
    else:
        print('Adivinaste, mi numero era:',numero)
        break