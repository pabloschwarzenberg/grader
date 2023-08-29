import time

def generar_numero_aleatorio():
    # Obtenemos la fecha y hora actual en segundos
    segundos_actuales = int(time.time())

    # Utilizamos la fecha y hora como semilla para generar el número pseudoaleatorio
    numero = ((segundos_actuales * 1103515245 + 12345) % (2**31))

    return numero

def jugar_adivina_mi_numero():
    numero_secreto = generar_numero_aleatorio() % 20 + 1
    intentos = 5

    print("Bienvenido al juego Adivina mi número!")
    print("Tienes 5 intentos para adivinar el número secreto, que está entre 1 y 20.")

    while intentos > 0:
        adivinanza = int(input("Ingresa tu número: "))

        if adivinanza == numero_secreto:
            print("¡Adivinaste! Mi número era", numero_secreto)
            return
        elif adivinanza < numero_secreto:
            print("Mi número es mayor.")
        else:
            print("Mi número es menor.")

        intentos -= 1

    print("No adivinaste. Mi número era", numero_secreto)

jugar_adivina_mi_numero()
