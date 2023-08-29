import random

aleatorio = random.randint(1,20)
cont = 0
control = True
while control:
    nUsuario = int(input("Adivina mi numero: "))
    if (nUsuario == aleatorio):
        print("Adivinaste, mi numero era:", aleatorio)
        control = False
    elif (nUsuario < aleatorio):
        print("Mi numero es mayor")
        cont = cont + 1
    elif (nUsuario > aleatorio):
        print("Mi numero es menor")
        cont = cont + 1
    if cont == 5:
        print("No adivinaste, mi numero era:",aleatorio)
        control= False