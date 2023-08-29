#Juego adivina mi número
import random
Nuestro_Nsecreto = random.randint(1, 20)

print("Bienvenido al juego Adivina mi número")
print("Tendras 5 intentos para adivinar el número secreto, que está entre 1 y 20.")

intentos = 0
while intentos < 5:
    # Solicitar el número al jugador
    numero_adivinar = int(input("Ingresa un número: "))

    intentos += 1

    if numero_adivinar < Nuestro_Nsecreto:
        print("Mi número es mayor.")
    elif numero_adivinar > Nuestro_Nsecreto:
        print("Mi número es menor.")
    else:
        print("¡Adivinaste! Mi número era", Nuestro_Nsecreto)
        break

if intentos == 5:
    print("No adivinaste. Mi número era", Nuestro_Nsecreto)
      