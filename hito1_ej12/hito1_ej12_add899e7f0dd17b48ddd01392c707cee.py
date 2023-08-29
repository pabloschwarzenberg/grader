#Juego adivina mi número
import random
intentosRealizados=0

numero=random.randint(1,20)
print("Estoy pensando en un número entre 1 y 20.")

while intentosRealizados<5:
    print("Intenta adivinar.")
    estimacion=input()
    estimacion=int(estimacion)

    intentosRealizados=intentosRealizados+1

    if estimacion<numero:
        print("Mi número es mayor.")

    if estimacion>numero:
        print("Mi número es menor.")

    if estimacion==numero:
        break

if estimacion==numero:
    intentosRealizados = str(intentosRealizados)
    print("¡Bien! ¡Has adivinado mi número en ", intentosRealizados, " intentos!")

if estimacion!=numero:
    numero=str(numero)
    print("No, el número que estaba pensando era", numero)