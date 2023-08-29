#Juego adivina mi número
from random import randrange
L =[]
L.append(randrange(1,20))
numero=L[0]
x=0
i=1
while i<6:
    x = int(input('ingresa un numero: '))
    if x>numero:
        print('Buscas un numero menor....')
    if x<numero:
        print('Buscas un numero mayor....')
    if x==numero:
        print('ADIVINASTE!!')
    i=i+1
print("No adivinaste, mi número era", numero)
