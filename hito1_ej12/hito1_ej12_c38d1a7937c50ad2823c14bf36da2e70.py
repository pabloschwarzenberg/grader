#Juego adivina mi numero
import random
aleatorio = random.randrange(20)
numero = int(input("Adivina el numero: "))
for i in range(4):
    if numero != aleatorio:
        if (numero < aleatorio):
            print("Mi numero es mayor")
        elif (numero > aleatorio):
            print("Mi numero es menor")
        numero = int(input("Ingrese nuevamente: "))
if numero == aleatorio:
        print("ADIVINASTE! Mi numero era ", aleatorio)
else:        
    print("No adivinaste, mi numero era", aleatorio)
      