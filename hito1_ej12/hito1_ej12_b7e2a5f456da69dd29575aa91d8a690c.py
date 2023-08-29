#Juego adivina mi número
#Crea un programa para el juego adivina mi número.
#Tú programa debe comenzar por generar aleatoriamente un número entre 1 y 20.
import random
num_min = 1
num_max = 20
num_sec = random.randint(num_min, num_max)    #número secreto
#El jugador tiene 5 intentos para adivinar el número
num_int = 0
while num_int < 5:
    num = int(input('Ingrese un número: '))    #número a adivinar
    num_int+=1
    if num > num_sec:
        print('Mi número es menor')
    elif num < num_sec:
        print('Mi número es mayor')
    elif num == num_sec:
       print('Adivinaste, mi número era:',num_sec)
       break
if num != num_sec:
    print('No adivinaste, mi número era:',num_sec)