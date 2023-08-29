from random import randint
numero = randint(1, 20)
flag = True
contador = 0
while flag:
    ingresa = eval(input("Numero: "))
    if ingresa == numero:
        print("Adivinaste, mi número era", numero)
        flag = False
    elif ingresa < numero:
        print("mi número es mayor")
        contador += 1
    elif ingresa > numero:
        print("mi número es menor")
        contador += 1
    if contador == 5:
        print("No adivinaste, mi número era", numero)
        flag = False