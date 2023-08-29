#Juego adivina mi número
import random
numero = random.randint(1,20)
intentos = 0

jugando = True

print("Adivina un numero, que se encuentra entre el 1 el 20")

while jugando:

    intentos += 1
    if intentos <= 5:
        eleccion = int(input("dime un numero "))
        if eleccion == numero:
            print("Adivinaste, mi numero era ",numero)
            jugando= False
        else:
            if eleccion > numero:
                print("mi numero es menor ")
            else:
                if eleccion < numero:
                    print("mi numero es mayor ")
    else:
        print("No adivinaste, mi numero era ", numero)
        jugando = False
        