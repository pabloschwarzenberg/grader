import random

# Generar un número aleatorio entre 1 y 20
numero_secreto = random.randint(1, 20)
intentos = 5

print("Bienvenido a 'Adivina mi número'!")
print("Tienes 5 intentos para adivinar el número secreto.")

while intentos > 0:
    # Solicitar al jugador que ingrese un número
    try:
        numero = int(input("Ingresa un número entre 1 y 20: "))
    except ValueError:
        print("Debes ingresar un número válido.")
        continue

    if numero == numero_secreto:
        print("¡Adivinaste! Mi número era", numero_secreto)
        break
      
    if numero < numero_secreto:
        print("Mi número es mayor.")
    else:
        print("Mi número es menor.")
    
    intentos -= 1

    if intentos == 0 or numero == numero_secreto:
        print("No adivinaste. Mi número era", numero_secreto)
        break

print("Gracias por jugar. ¡Hasta la próxima!")

