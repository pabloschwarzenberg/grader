#Juego adivina mi número
import random
intentos = 0

n = random.randint(1, 20)
print("Adivina mi numero entre 1 y 20")

while intentos < 5:
    numero = int(input())
    intentos = intentos + 1
    if numero < n:
        print("Mi número es mayor")
    if numero > n:
        print("Mi número es menor ")
    if numero == n:
        break
if numero == n:
    print("Adivinaste, mi número era", n)
else:
    print("No adivinaste, mi número era", n)    