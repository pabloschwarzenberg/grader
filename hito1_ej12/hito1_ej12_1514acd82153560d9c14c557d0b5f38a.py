#Juego adivina mi número
import random

Numero_de_intentos = 0
Numero_minimo = 1
Numero_maximo = 20

aleatorio = random.randint(Numero_minimo,Numero_maximo)
print("Adivina un número entre" + str(Numero_minimo) + "y" + str(Numero_maximo))

while Numero_de_intentos <5:
    print("tu número es: ")
    respuesta = input()
    respuesta = int(respuesta)

    Numero_de_intentos = Numero_de_intentos + 1

    if respuesta < aleatorio:
        print("Mi número es mayor: ")
    if respuesta > aleatorio:
        print ("Mi número es menor: ")
    if  respuesta == aleatorio:
        break

if respuesta == aleatorio:
    print("Adivinaste, mi número era:" + str(aleatorio))

if respuesta != aleatorio:
    print("No adivinaste, mi número era:" + str(aleatorio))
     