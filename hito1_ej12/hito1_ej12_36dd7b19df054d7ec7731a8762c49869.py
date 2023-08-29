#Juego adivina mi número
import random
secreto = random.randint(1,20)
for i in range(0,5):
    numero = int(input('Ingrese un número: '))
    if secreto > numero:
        print('Mi número es mayor')
    if secreto < numero:
        print('Mi número es menos')
    if secreto == numero:
        print('Adivinaste, mi número era', secreto)
        break
    if secreto != numero and i == 4:
        print('No adivinaste, mi número era', secreto)