#Juego adivina mi número
import sys
import random
print("Bienvenido a <Adivina mi número>")
secreto = random.randint(1,20)
for i in range(5):
    print("Tienes",5-i,"intentos")
    jugador = int(input("Ingresa el número que creas es mi número><: "))
    if secreto > jugador and 5-i>1:
        print("mi número es mayor")
    elif secreto < jugador and 5-i>1:
        print("mi número es menor")
    elif secreto == jugador:
        print("Adivinaste, mi número era ",secreto)
        sys.exit("")
    else:
        break
print("No adivinaste, mi número era ",secreto)      