#Juego adivina mi número
import random

aleatorio = random.randint(1, 20)
intentos = 5

resultado = False

while intentos > 0:
    n = int(input("Adivina mi numero: "))
    
    if n > aleatorio:
        print("mi número es menor")
    elif n < aleatorio:
        print("mi número es mayor")

    if n == aleatorio:
        resultado = True
        break

    intentos -= 1

if resultado:
    print('Adivinaste, mi número era {}'.format(aleatorio))
else:
    print('No adivinaste, mi número era {}'.format(aleatorio) )
