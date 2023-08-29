import random

numero_secreto = random.randint(1, 20)
intentos = 5

print("¡Bienvenido al juego Adivina mi número!")
print("Tienes 5 intentos para adivinar un número entre 1 y 20.")

while intentos > 0:
    intento = int(input("Ingresa tu número: "))
    
    if intento == numero_secreto:
        print("Adivinaste, mi número era", numero_secreto)
        break
    elif intento < numero_secreto:
        print("Mi número es mayor")
    else:
        print("Mi número es menor")
    
    intentos -= 1
    
    if intentos == 0:
        print("No adivinaste, mi número era", numero_secreto)
