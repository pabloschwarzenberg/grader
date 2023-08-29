#Juego adivina mi número
import random
n=random.randint(1,20)
for i in range(5) :
    jugador=int(input("Ingrese un numero: "))
    if jugador==n :
        print("Ganaste, felicitaciones!!")
    elif jugador>n :
        print("Incorrecto, el numero es menor")
    elif jugador<n :
        print("Incorrecto, el numero es mayor")
if jugador!=n :
    print("Perdiste, nos vemos!")
      