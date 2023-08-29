#Juego adivina mi número
import random

intentos = 0
minimo = 1
maximo = 20

print("adivina mi numero")

n = random.randint(minimo , maximo)

print("mi numero esta entre el " , str(minimo) , "y" , str(maximo))
print("ojo tienes 5 intentos")

while intentos < 5:
    intenta = input("intenta adivinarlo : " )
    intenta = int(intenta)
    intentos = intentos + 1

    if intenta < n:
        print("mi número es mayor")
    if intenta > n:
        print("mi número es menor")
    if intenta == n:
        break

if intenta == n:
    print("Adivinaste mi numero era :" , n )

if intenta != n:
    print("No adivinaste mi numero era :" , n)
    
    
