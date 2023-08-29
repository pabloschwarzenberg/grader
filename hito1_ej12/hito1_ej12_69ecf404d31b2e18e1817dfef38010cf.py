import random
n = random.randint(1,20)
def adivina (n):
    contador = 0
    while contador < 5:
        intentos = int(input())
        if intentos == n:
            print("Adivinaste, mi numero era " + str(n))
            contador = contador + 1
            break
        if intentos < n:
            print("Mi numero es mayor")
            contador = contador + 1
        if intentos > n :
            print("Mi numero es menor")
            contador = contador + 1
        if contador > 5:
            print("No adivinaste, mi numero era " + str(n))
            break
adivina(n)