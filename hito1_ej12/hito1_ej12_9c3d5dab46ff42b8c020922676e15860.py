#Juego adivina mi número
import random
intentosRealizados = 0
numero = random.randint(1, 20)
print("estoy pensando en un numero entre 1 y 20:")

while intentosRealizados < 5:

    estimacion = input()

    estimacion = int(estimacion)


    intentosRealizados = intentosRealizados + 1



    if estimacion < numero:

        print("mi numero es mayor:")



    if estimacion > numero:

         print("mi numero es menor:")
         
         if estimacion == numero:
             break



if estimacion == numero:

     print("Has adivinado mi número es:", numero)


if estimacion != numero:

     print("No adivinaste, mi numero era:", numero)