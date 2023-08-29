#Juego adivina mi número
import random

nSecreto = random.randint(1,20)
adivinaste = 0
for i in range (0,5):
    numero = int(input("Ingrese numero: "))
    if numero > nSecreto:
        print("el numero es menor")
    elif numero < nSecreto:
        print("el numero es mayor")
    else:
        print("adivinaste, el numero era: ", nSecreto)
        break
if adivinaste != 1:
    print("no adivinaste, el numero era :", nSecreto)
else:
    print("ADIOS")