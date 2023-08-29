import random

intentosrealizados = 0

numero = random.randint(1, 20)
print(" Estoy pensando en un numero del 1 al 20")

while intentosrealizados < 5:
    intentos = int(input("Intenta adivinar: "))

    intentosrealizados = intentosrealizados + 1

    if intentos < numero:
        print("Mi numero es mayor")
    elif intentos > numero:
        print("Mi numero es menor")

if intentos == numero:
    intentosrealizados = str(intentosrealizados)
    print("Adivinaste, mi número era",numero)
elif intentos != numero:
    numero = str(numero)
    print("No adivinaste, mi numero era",numero)    