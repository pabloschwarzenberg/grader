#Juego adivina mi número
import random
def adivina_mi_numero():
    n_secreto = random.randint(1, 20)
    intentos = 5
    print("Bienvenido al juego Adivina mi número!")
    print("Tienes 5 intentos para adivinar el número secreto (entre 1 y 20).")
    while intentos > 0:
        intento = int(input("Ingresa un número: "))
        if intento == n_secreto:
            print("Adivinaste, mi número era", n_secreto)
            return
        elif intento < n_secreto:
            print("Mi número es mayor.")
        else:
            print("Mi número es menor.")
        intentos -= 1
        print("Te quedan", intentos, "intentos.")
    print("No adivinaste, mi número era", n_secreto)
adivina_mi_numero()
      