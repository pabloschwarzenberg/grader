#Juego adivina mi número
import random

numero_secreto = random.randint(1, 20)
intentos = 5

print("Bienvenido al juego 'Adivina mi número'!")
print("He generado un número entre 1 y 20. Tienes 5 intentos para adivinarlo.")

for i in range(intentos):
    print("\nIntento", i + 1)
    numero_adivinar = int(input("Ingresa tu número: "))
    
    if numero_adivinar < numero_secreto:
        print("Mi número es mayor.")
    elif numero_adivinar > numero_secreto:
        print("Mi número es menor.")
    else:
        print("¡Adivinaste! Mi número era", numero_secreto)
        break

if numero_adivinar != numero_secreto:
    print("\nNo adivinaste. Mi número era", numero_secreto)
