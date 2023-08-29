#Juego adivina mi número
print("Adivina mi número")
import random

numero = random.randint(1,20)
intentos = 0

juego = True

print("Adivina un numero del 1 al 20")

while juego:
    intentos >= 1 
    if intentos <=5:

        eleccion = int(input("Ingresa un numero: "))
        if eleccion == numero:
            print("Adivinaste, mi número era :", numero)
            juego = False
        elif eleccion > numero:
            print("Mi número es menor.") 
        elif eleccion < numero:
            print("Mi número es mayor.")
   
    else:
        print("No adivinaste, mi número era: ", numero)
        juego = False