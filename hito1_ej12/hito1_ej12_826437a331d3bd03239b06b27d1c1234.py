#Juego adivina mi número
import random
class juego:
    vida = 5
    numero = random.randint(1, 20)
    def ronda():
        while True:
            respuesta = int(input("Ingrese un numero entre 1 y 20: "))
            if respuesta == juego.numero:
                print("Adivinaste, mi número era", juego.numero)
                break
            elif respuesta > juego.numero:
                print("mi número es menor")
                juego.vida -= 1
            elif respuesta < juego.numero:
                print("mi número es mayor")
                juego.vida -= 1
            if juego.vida == 0:
                print("No adivinaste, mi número era ", juego.numero)
                break
juego.ronda()      