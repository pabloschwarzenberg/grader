#Juego adivina mi número
import random
numero_aleatorio = random.randrange(21)
intentos = 5
while intentos > 0:
    numero_adivinado = int (input("Ingrese el Numero Adivinado: "))
    if numero_adivinado == numero_aleatorio:
        print("Adivinaste, mi numero era ",numero_aleatorio)
        break
    elif numero_adivinado != numero_aleatorio:
        intentos = intentos - 1
        if numero_adivinado < numero_aleatorio:
            print("Mi numero es Mayor")
        elif numero_adivinado > numero_aleatorio:
            print("Mi numero es Menor")
else:
    print("No adivinaste, mi numero era:",numero_aleatorio)




