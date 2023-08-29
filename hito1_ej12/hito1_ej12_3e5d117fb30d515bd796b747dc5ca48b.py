import random
intento = 1
numero = random.randint(1, 20)
while intento < 6:
    adivina = int(input())
    if intento == 5:
        if numero == adivina:
            print("Adivinaste, mi número era", numero)
        else:
            print("No adivinaste, mi número era", numero)
    else:
        if numero == adivina:
            print("Adivinaste, mi número era", numero)
        elif numero > adivina:
            print("Mayor")
        else:
            print("Menor")
    intento = intento + 1