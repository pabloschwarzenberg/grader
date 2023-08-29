import random
numero = random.randint(1, 20)
vidas = 5
while vidas != 0:
    adivina = int(input("Ingrese un numero:"))
    if adivina > numero:
        print("mi número es menor")
        vidas = vidas-1
    if numero > adivina:
       print("mi número es mayor")
       vidas = vidas - 1
    if adivina == numero:
        print("Adivinaste, mi número era", numero)
        break
    if vidas == 0:
        print("No adivinaste, mi número era ", numero)


