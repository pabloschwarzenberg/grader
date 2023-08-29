import random
intentosRealizados = 0
numero = random.randint(1, 20)
while intentosRealizados < 5:
    print('Intenta adivinar!!')
    estimacion = input()
    estimacion = int(estimacion)
    intentosRealizados = intentosRealizados + 1
    if estimacion > numero:
        print('mi número es menor')
    if estimacion < numero:
        print('mi número es mayor')
    if estimacion == numero:
        break
if estimacion == numero:
    intentosRealizados = str(intentosRealizados)
    print('Adivinaste, mi número era ' + str(numero))
if estimacion != numero:
    numero = str(numero)
    print('No adivinaste, mi número era ' + str(numero))