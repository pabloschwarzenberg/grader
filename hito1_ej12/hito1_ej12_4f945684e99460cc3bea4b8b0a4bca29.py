#Juego adivina mi número
import random

intentosRealizados = 0

print("¡Hola! ¿Cómo te llamas?")
x = input()

numero = random.randint(1, 20)
print("Buneo, {}, estoy pensando en un numero entre 1 y 20".format(x))

while intentosRealizados < 5:
    print("Intenta adivinar")
    estimacion = input()
    estimacion = int(estimacion)

    intentosRealizados = intentosRealizados + 1

    if estimacion < numero:
        print("Tu estimación es muy baja.")

    if estimacion > numero:
        print("Tu estimación es muy alta.")

    if estimacion == numero:
        break

if estimacion == numero:
    intentosRealizados = str(intentosRealizados)
    print("¡Buen trabajo, " + x + "! ¡Has adivinado mi número en " + intentosRealizados + " intentos!")

if estimacion != numero:
    numero = str(numero)
    print("Pues no. El número que estaba pensando era " + numero)