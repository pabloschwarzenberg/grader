#Juego adivina mi número
import random
numero=random.randint(1,20)
intentos=5
while not intentos==0:
    if intentos!=0:
        ingresar = int(input("ingresar numero: "))
        if ingresar > numero:
            print("Mi numero es menor")
        if ingresar<numero:
            print("Mi numero es mayor")
        if ingresar == numero:
            print("Adivinaste, mi numero era ",numero)
            break
        intentos = intentos - 1
    if intentos==0:
        print("No Adivinaste, mi numero era ",numero)
      