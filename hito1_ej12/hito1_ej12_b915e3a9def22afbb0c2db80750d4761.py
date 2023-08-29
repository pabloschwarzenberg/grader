#Juego adivina mi número
import random
numero = random.randint (1,20)
intentos = 5
while True:
    respuesta = int(input("ingresa numero:"))
    if(respuesta > numero):
        print("el numero mio es menor")
    if(respuesta < numero):
        
        print("el numero es mio es mayor")
    if(respuesta == numero):
        print("Adivinaste, mi número era ", numero)
        break = intentos 