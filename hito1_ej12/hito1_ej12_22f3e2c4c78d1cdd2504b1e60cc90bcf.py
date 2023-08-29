#Juego adivina mi número
import random
numsec = random.randint(1,20)
print("Adivina mi número entre 1 y 20, tienes 5 intentos.")
for i in range(1,6):
    numero=int(input("Intento {i}\nIngresa un numero entre 1 y 20: "))
    if numero < numsec:
        print("El numero es mayor.")
    elif numero > numsec:
        print("El número es menor.")
    elif numero == numsec:
        print("Adivinaste, mi número era:",numsec)
        break
if numero != numsec:
    print("No adivinaste, mi número era:",numsec)     