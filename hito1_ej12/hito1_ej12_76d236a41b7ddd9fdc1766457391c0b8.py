#Juego adivina mi número
import random
intentosRealizados = 0
print('¡Hola! ¿Cómo te llamas?')
miNombre = input()
numero = random.randint(1, 20)
print('Bueno, ' + miNombre + ', estoy pensando en un numero entre 1 y 20.')
while intentosRealizados < 5:
    estimacion = int(input('Intenta adivinar.'))
    intentosRealizados = intentosRealizados + 1
    if estimacion < numero:
        print('Mi numero es mayor') 
    if estimacion > numero:
        print('Mi numero es menor')
    if estimacion == numero:
         break
if estimacion == numero:
    intentosRealizados = str(intentosRealizados)
    print('Adivinaste, mi numero era ', numero)
if estimacion != numero:
    numero = numero
    print('No adivinaste, mi número era ', numero)
