#Juego adivina mi número
import random

numero = random.randint(1, 20)
print("Estoy pensando en un numero entre 1 y 20")
intentos = 0

while intentos < 5:
    print('Intenta adivinar.') 
    estimacion = input()
    estimacion = int(estimacion)
    intentos = intentos + 1
    if estimacion < numero:
        print("Mi número es mayor") 
    elif estimacion > numero:
             print("Mi número es menor")
    else:
        break
if estimacion == numero:
    print("Adivinaste, mi número era", numero)

if estimacion != numero:
    print("No adivinaste, mi número era ", numero)