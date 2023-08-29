#Juego adivina mi número
import random
n = random.randint(1,20)
print(n)

numero = 0 
intento = 5 

while numero != n:
    numero = int(input("adivina el numero"))
    if numero > n:
        print("mi número es menor")
    if numero < n:
        print(" mi número es mayor")
    intento = intento - 1 
    if numero == n:
        print("Adivinaste, mi número era", n)
    elif intento ==0:
        print("No adivinaste, mi número era", n)
        break   
     