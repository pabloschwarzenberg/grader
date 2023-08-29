#Juego adivina mi número
import random
inicio = random.randint(1, 20)
cont = 0
print(inicio)
while True:
    numero = int(input("ingrese un numero entre 1 y 20: "))
    if numero == inicio:
        print("Adivinaste, mi número era",inicio)
        break
    if numero != inicio:
        cont = cont + 1
        if numero < inicio:
            print("mi numero es mayor")
        if numero > inicio:
            print("mi numero es menor")
    if cont == 5:
        print("No adivinaste, mi número era",inicio)
        break
