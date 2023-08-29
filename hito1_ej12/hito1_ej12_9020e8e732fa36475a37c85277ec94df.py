intentos = 5

print("¡Bienvenido al juego Adivina mi número!")
print("Tienes que adivinar un número entre 1 y 20. ¡Buena suerte!")

numero_secreto = int(input("Ingresa el número secreto: "))

for i in range(intentos):
    try:
        numero_ingresado = int(input("Intento : Ingresa un número: ".format(i+1)))
    except ValueError:
        print("Debes ingresar un número válido.")
        continue

    if numero_ingresado == numero_secreto:
        print("¡Adivinaste, mi número era", numero_secreto, "!")
        break
    elif numero_ingresado < numero_secreto:
        print("Mi número es mayor")
    else:
        print("Mi número es menor")

if numero_ingresado != numero_secreto:
    print("No adivinaste, mi número era", numero_secreto, ". ¡Mejor suerte la próxima vez!")