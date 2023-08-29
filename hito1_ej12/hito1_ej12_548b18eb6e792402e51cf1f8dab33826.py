from random import randint


i = 0
numero_aleatorio = randint(1,20)

while i < 5:
    i += 1
    numero = eval(input("Ingrese el número: "))
    if numero == numero_aleatorio:
        print("Adivinaste, mi numero era ",numero_aleatorio)
        break
    elif numero < numero_aleatorio:
        print("mi número es mayor")
    elif numero > numero_aleatorio:
        print("mi número es menor")

if numero != numero_aleatorio:
    print("No adivinaste, mi numero era ",numero_aleatorio)