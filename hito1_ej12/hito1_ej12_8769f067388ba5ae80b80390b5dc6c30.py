#Juego adivina mi número
import random
numero = random.randint(1,20)
intento = 0
intentos = 0
jugando = True
while jugando == True:
    intento = int(input("Adivina mi número: "))
    if intento < numero:
        print("mi número es mayor")
    if intento > numero:
        print("mi número es menor")
    intentos += 1
    if intento == numero:
        print("Adivinaste, mi número era: ", numero)
        jugando = False
    if intentos == 5:
        print("No adivinaste, mi número era: ", numero)
        jugando = False