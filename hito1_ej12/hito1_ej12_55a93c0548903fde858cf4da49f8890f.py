#Juego adivina mi número
import random
def adivina():
    s = random.randint(1,20)
    a = 0
    while a < 5:
        n = int(input("Ingrese un numero: "))
        if n == s:
            print("Adivinaste, mi numero era: ",n)
            break
        elif n < s:
            print("Mi numero es mayor")
        elif n > s:
            print("Mi numero es menor")
        if a == 5:
            print("No adivinaste, mi numero era", n)
        a += 1
    return
print(adivina())