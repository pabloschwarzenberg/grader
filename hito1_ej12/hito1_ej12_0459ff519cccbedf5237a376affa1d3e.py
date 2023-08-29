#Juego adivina mi número
#Juego adivina mi número
import random
intentos=0
num = random.randint(1,20)
respuesta = 0
while True:
    respuesta = int(input("intenta adivinar el numero!:"))
    intentos = intentos + 1
    if respuesta < num:
        print("mi numero es mayor")
    if respuesta > num:
        print("mi numero es menor")
    if respuesta == num:
        break
    if intentos >4:
        break
if respuesta == num:
    print("Adivinaste, mi número era:",num)
if respuesta != num:
    print("No adivinaste, mi número era:",num)     