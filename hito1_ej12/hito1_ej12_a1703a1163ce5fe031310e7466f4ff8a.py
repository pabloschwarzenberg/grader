import random

n_secreto = random.randint(1, 20)

print('¡Bienvenido al juego Adivina mi número!')
print('Tienes 5 intentos para adivinar el número secreto (entre 1 y 20).')

intentos = 0
adivinado = False

while intentos < 5:
    intentos = intentos + 1
    numero_ingresado = int(
        input('Intento #' + str(intentos) + ': Ingresa un número: '))

    if numero_ingresado == n_secreto:
        adivinado = True
        break
    elif numero_ingresado < n_secreto:
        print('Mi número es mayor.')
    else:
        print('Mi número es menor.')

if adivinado:
    print('¡Adivinaste! Mi número era', n_secreto)
else:
    print('No adivinaste. Mi número era', n_secreto)

