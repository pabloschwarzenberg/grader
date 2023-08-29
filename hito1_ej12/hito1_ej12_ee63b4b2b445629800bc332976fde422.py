#Juego adivina mi número
import random
numero =int(input(" ingrese el numero para jugar :"))

secreto = random.randint(1,20)

while numero > 0 :
    if numero == secreto :
        print (" Adivinaste, mi numero era ", secreto)
        break


    elif numero > secreto :
        print (" mi numero es menor")
        numero = int(input(" ingrese el numero para jugar :"))


    elif numero < secreto :
        print (" mi numero es mayor")
        numero = int(input(" ingrese el numero para jugar :"))


while numero < 0 :
    print (" error intente de nuevo")
    break