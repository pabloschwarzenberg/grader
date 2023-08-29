#Juego adivina mi número
import random
intentos = 0

numero = random.randint(1, 20)
print("Adivina un numero entre 1 y 20")

while intentos < 5:
    respuesta = int(input())
    intentos = intentos + 1
    if respuesta < numero:
        print("Mi numero es mayor")
    if respuesta > numero:
        print("Mi numero es menor ")
    if respuesta == numero:
        break
if respuesta == numero:
    print("Adivinaste, mi numero era", numero)
if respuesta != numero:
    print("No adivinaste, mi numero era", numero)
    
      