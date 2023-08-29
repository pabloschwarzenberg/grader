#Juego adivina mi número
import random

numero_secreto = random.randint(1, 20)
intentos = 5

print("¡Bienvenido a Adivina mi Número!")
print("Tienes 5 intentos para adivinar mi número, que está entre 1 y 20.")
print("¡Suerte!")

while intentos > 0:
    print("Intento #" + str(6 - intentos))
    guess = int(input("Ingresa tu número: "))
    
    if guess == numero_secreto:
        print("¡Adivinaste, mi número era " + str(numero_secreto) + "!")
        break
    elif guess < numero_secreto:
        print("Mi número es mayor.")
    else:
        print("Mi número es menor.")
        
    intentos -= 1

if intentos == 0:
    print("Lo siento, no adivinaste en los 5 intentos.")
    print("Mi número era " + str(numero_secreto) + ".")
