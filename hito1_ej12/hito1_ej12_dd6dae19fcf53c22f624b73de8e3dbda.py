#Juego adivina mi número
import random

numero= random.randint(1,20)

adivinaste=0


for i in range (0,5):
    numeroUsuario=int(input("Ingrese número entre 0 y 20"))
    if numeroUsuario > numero:
        print("Mi número es menor")

    elif numeroUsuario < numero:
        print("Mi número es mayor")

    else:
        adivinaste=1
        print("Adivinaste, mi número era: ",numero)
        break

if adivinaste !=1:
    print("No adivinaste, mi número era: ",numero)

      