#Juego adivina mi número
      import random

numero_secreto = random.randint(1, 20)
intentos_restantes = 5

print("¡Bienvenido al juego Adivina mi número!")
print("Tienes 5 intentos para adivinar el número secreto, que está entre 1 y 20.")

while intentos_restantes > 0:
    numero_ingresado = int(input("Ingresa un número: "))
    
    if numero_ingresado == numero_secreto:
        print("¡Adivinaste, mi número era", numero_secreto, "!")
        break
    elif numero_ingresado < numero_secreto:
        print("Mi número es mayor.")
    else:
        print("Mi número es menor.")
    
    intentos_restantes -= 1
    print("Intentos restantes:", intentos_restantes)

if intentos_restantes == 0:
    print("No adivinaste, mi número era", numero_secreto, ". ¡Mejor suerte la próxima vez!")
