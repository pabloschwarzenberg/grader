#Juego adivina mi número
import random
i=0
numero = random.randint(1,20)
while i < 5:
    i = i+1
    n= int(input("Ingresa un numero: "))
    if n == numero:
        print('Adivinaste, mi numero era'),numero
        break
    elif numero > n:
        print("mi numero es mayor")
    elif numero < n:
        print("mi numero es menor")
    if i==5:
        print('mi numero era',numero)