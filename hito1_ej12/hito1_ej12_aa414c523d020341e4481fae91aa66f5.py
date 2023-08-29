#Juego adivina mi número
import random
a = random.randrange(21)
i1 = int(input('Primer intento: '))
if i1 == a:
    print('Adivinaste, mi numero era', a)
elif i1 != a:
    if i1 > a:
        print(i1 , 'es menor que mi numero')
    if i1 < a:
        print(i1, 'es mayor que mi numero')
i2 = int(input('Segundo intento: '))
if i2 == a:
    print('Adivinaste, mi numero era', a)
elif i2 != a:
    if i2 > a:
        print(i2, 'es menor que mi numero')
    if i2 < a:
        print(i2 , 'es mayor que mi numero')
i3 = int(input('Tercer intento: '))
if i3 == a:
    print('Adivinaste, mi numero era', a)
elif i3 != a:
    if i3 > a:
        print(i3 , 'es menor que mi numero')
    if i3 < a:
        print(i3, 'es mayor que mi numero')
i4 = int(input('Cuarto intento: '))
if i4 == a:
    print('Adivinaste, mi numero era', a)
elif i4 != a:
    if i4 > a:
        print(i4 , 'es menor que mi numero')
    if i4 < a:
        print(i4, 'es mayor que mi numero')
i5 = int(input('Quinto intento: '))
if i5 == a:
    print('Adivinaste, mi numero era', a)
else:
    print('No adivinaste, mi número era', a)