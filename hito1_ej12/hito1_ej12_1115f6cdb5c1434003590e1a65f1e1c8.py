#Juego adivina mi número
import random
numero = (random.randrange(1, 20))
intentos = 1
IngresarNumero= int(input("Ingrese un número: "))

while (IngresarNumero != numero and intentos != 5):
    if (IngresarNumero < numero):
        print("El número ingresado es menor al número a adivinar")
        intentos += 1
        IngresarNumero= int(input("Ingrese un número: "))

    elif (IngresarNumero > numero):
        print("El número ingresado es mayor al número a adivinar")
        intentos += 1
        IngresarNumero= int(input("Ingrese un número: "))

if (IngresarNumero == numero):
    print("Adivinaste, mi número era ", numero)

elif (intentos == 5):
    print("No adivinaste, mi número era ",numero )      