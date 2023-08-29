#Juego adivina mi número
intentos=0
import random
n=random.randint(1,20)
print (n)
while intentos<5:
    a=int(input('intenta adivivinar el mi numero, ingresa un numero: '))
    if a<n:
        print('tu numero es menor')
    elif a>n:
        print('tu numero es mayor')
    elif a==n:
        print('Adivinaste mi numero era: ',n)
        intentos=6
    else:
        print('no adivinaste, mi numero era',n) 
    intentos=intentos+1