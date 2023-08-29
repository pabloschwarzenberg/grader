# Juego adivina mi numero
# Importaciones
import random
# Entrada
secreto = random.randint(1, 20)
print(secreto)
intentos = 1
num = 0
# Proceso
while intentos <= 5 and num != secreto:
    num = int(input("Ingrese su numero: "))
    if num != secreto:
        if num < secreto:
            print("*** Mi numero es menor al secreto ***")
        elif num > secreto:
            print("*** Mi numero es mayor al secreto *** ")
    else:
        if num == secreto:
            print("Adivinaste, mi numero era", secreto)
        elif intentos == 5:
            print("No adivinaste, mi numero era", secreto)

    intentos += 1