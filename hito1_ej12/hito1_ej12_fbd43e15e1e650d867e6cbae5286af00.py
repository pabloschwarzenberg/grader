#Juego adivina mi número
import random
listado = list(range(1,21))
num = random.choice(listado)

numero = 0
n = 0

while numero != num and n < 5:
    numero = int(input("Ingrese un numero de 1 a 20: "))
    if numero < num:
        print("Ingrese un numero mayor")
    if numero > num:
        print("Ingrese un numero menor")
    n += 1

if numero != num:
    print("No adivinaste, mi numero era",num)

elif numero == num:
    print("Adivinaste, mi numero era",num)      