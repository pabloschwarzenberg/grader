import random
min=1
max=20
numero_secreto=random.randint(min,max)
print(numero_secreto)
intentos=1

while intentos<=5:
    numero = eval(input("Ingresa el numero : "))

    if numero<numero_secreto:
        print('mi número es menor ')
    else:
        print('mi número es mayor')
    if numero==numero_secreto:
        print('divinaste, mi número era ',numero_secreto)
        break
    intentos=intentos+1


if intentos>5:
    print('No adivinaste, mi número era',numero_secreto)
      