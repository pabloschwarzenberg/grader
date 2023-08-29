#Juego adivina mi número
import random
x = random.randint(1,21)
n = 0

while n <= 5:
    y = int(input("Adivina mi número, ¿Cuál crees que es?: "))
    if y == x:
        print("Adivinaste, mi número era",x)
        break
    if x < y:
        print("mi número es menor")
        n += 1
    if x > y:
        print("mi número es mayor")
        n += 1
    if n == 5:
        print("No adivinaste, mi número era",x)
        break      