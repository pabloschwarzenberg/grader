#Juego adivina mi número
import random

numeroSecreto = random.randrange(20)
contador = 0
for i in range(5):
    numeroIngresado = int(input("Ingresa un numero: "))
    if(numeroIngresado == numeroSecreto):
        print("Adivinaste, mi número era ", numeroSecreto)
        break
    else:
        contador += 1
        if(numeroIngresado > numeroSecreto):
            print("mi número es menor")
        elif(numeroIngresado < numeroSecreto):
            print("mi número es mayor")

if(contador == 5):
    print("No adivinaste, mi número era ", numeroSecreto)

