#Juego adivina mi número
import random
intentos=0
n = random.randint(1,20)
print("piensa un número entre 1 y 20: ")

while intentos < 5:
    print ("Adivina el numero, Tienes 5 intentos: ")
    adivina = input()
    adivina = int(adivina)

    intentos = intentos+1
   
    if adivina < n:
        print ("el numero es MAYOR a este: ")

    if adivina > n:
        print("El numero es MENOR a este: ")
    

if adivina==n:
    intentos=str(intentos)
    print("Adivinaste, mi número era: ", +n)

if adivina!=n:
    numero=str(n)
    print("No adivinaste, mi número era", +n)
