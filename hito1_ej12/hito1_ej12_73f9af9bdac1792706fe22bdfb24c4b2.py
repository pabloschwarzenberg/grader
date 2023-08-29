#Juego adivina mi número
import random
cant_intentos = 5
numero_adivinar = random.randint(1, 20)

while cant_intentos > 0:
    intento = int(input("Ingrese un numero para adivinar: "))
    if intento > numero_adivinar:
        print("mi número es menor")
        cant_intentos=cant_intentos-1
    elif intento < numero_adivinar:
        print("mi número es mayor")
        cant_intentos=cant_intentos-1
    elif intento == numero_adivinar:
        print("Adivinaste, mi número era ", numero_adivinar)
        quit()
if cant_intentos == 0:
    print("No adivinaste, mi número era ", numero_adivinar)