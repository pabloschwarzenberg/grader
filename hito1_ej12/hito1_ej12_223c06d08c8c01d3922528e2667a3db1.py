#Juego adivina mi número
import random
intentos = 0
numeroram = random.randint(1, 20)
print(numeroram)
print("Escoje un numero entre 1 y el 20")
while intentos < 5:
    numero = int(input("intenta "))
    intentos = intentos + 1
    if (numero > numeroram):
        print("mi número es menor")
    elif (numero < numeroram):
        print("mi número es mayor")
    elif (numero == numeroram):
        break
if (numero == numeroram):
    print("Adivinaste, mi número era", numeroram)

else:
    print("No adivinaste, mi número era", numeroram)