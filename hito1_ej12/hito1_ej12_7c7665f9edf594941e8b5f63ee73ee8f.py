from random import randint
n = randint(1, 21)
contador = 0
numero= 0
while numero != 500:

    if numero < n:
        print("Mi número es mayor")
    if numero > n:
        print("Mi número es menor")
    numero = int(input("Ingrese número: "))
    contador = contador + 1
    if contador == 5:
        print("No adivinaste, mi número era", n)
        break
    if numero == n:
        print("Adivinaste, mi número era", n)
        break