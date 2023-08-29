#Juego adivina mi número
import random
def adivina_numero():
    numero_secreto = random.randint(1, 20)
    intentos = 5
    print("Bienvenido al juego Adivina mi número")
    print("Tienes 5 intentos para adivinar el número secreto entre el 1 y el 20")
    while intentos > 0:
        Intento = int(input("Ingresa un número: "))
        if Intento == numero_secreto:
            print("Adivinaste, mi número era", numero_secreto)
            return
        elif Intento < numero_secreto:
            print("El número es mayor")
        else:
            print("El número es menor")
        intentos -= 1
        print("Te quedan", intentos, "intentos")
    print("No adivinaste, mi número era", numero_secreto)
adivina_numero()      
      