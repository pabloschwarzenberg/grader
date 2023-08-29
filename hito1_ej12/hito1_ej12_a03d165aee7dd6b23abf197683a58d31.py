#Juego adivina mi número
import random
numero_secreto = random.randint(1,20)
for i in range(0,5):
    numero = int(input("Bienvenido a Adivina mi numero, Ingrese un numero: "))
    if numero > numero_secreto:
        print("Mi numero es menor, intenta nuevamente")
    elif numero < numero_secreto:
        print("Mi numero es mayor, intenta nuevamente")
    else:
        print("Adivinaste!!!, Mi numero era ",numero_secreto)
        break
print("No adivinaste, Mi numero era ",numero_secreto)