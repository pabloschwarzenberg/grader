#Juego adivina mi número
import random
intentos_realizados=0
numero = random.randint(1,20)
estimacion = 0
while True:
    estimacion = int(input("intenta adivinar!:"))
    intentos_realizados = intentos_realizados + 1
    if estimacion < numero:
        print("mi numero es mayor")
    if estimacion > numero:
        print("mi numero es menor")
    if estimacion == numero:
        break
    if intentos_realizados >4:
        break
if estimacion == numero:
    print("Adivinaste, mi número era:",numero)
if estimacion != numero:
    print("No adivinaste, mi número era:",numero)