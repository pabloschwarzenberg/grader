#Juego adivina mi número
import random
ns = random.randint(1,20)
i = 0
ni = 0
print(ns)
while i <5:
    if ni != ns :
        ni = int(input('ingrese un numero: '))
        i+=1
        if ni > ns:
            if i ==5:
                print('no adivinaste, mi número era ',ns)
            else:
                print('mi número es menor')
        elif ni < ns :
            if i == 5:
                print('no adivinaste, mi número era ',ns)
            else:
                print('mi número es mayor')
    elif ni != ns:
        print('no adivinaste, mi número era ',ns)
        break
    else:
        break

if ni == ns :