#Juego adivina mi número
import random

def juego():
    vidas = 5
    num = random.randint(1,20)
   
    while True:
        if vidas > 0:
            num2 = int(input("Ingrese un numero "))
            if num2 == num:
                print("Adivinaste, mi número era "+ str(num))
                break
            elif num > num2:
                print("mi número es mayor")
                vidas -= 1
            elif num < num2:
                print("mi número es menor")
                vidas -= 1
        elif vidas == 0:
            print("No adivinaste,mi número era " + str(num))
            break

juego()      