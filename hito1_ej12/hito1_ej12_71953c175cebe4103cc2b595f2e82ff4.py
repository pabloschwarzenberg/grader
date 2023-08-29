#Juego adivina mi número
import random
numeroSecreto = random.randint(1,20)
adivinaste = 0
for i in range(0,5):
    numero = int(input("Ingrese numero: "))
    if numero > numeroSecreto:
        print("Mi numero es menor")
    elif numero < numeroSecreto:
        print("Mi numero es Mayor")
    else:
        adivinaste = 1
        print("Adivinaste, mi número era ", numeroSecreto)
        break
if adivinaste != 1:
    print("No adivinaste, mi número era ", numeroSecreto)
