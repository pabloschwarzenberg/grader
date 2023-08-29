import random

def adivinanro():
    nro = random.randint(1, 20)
    intentos = 5

    print("Bienvenido a 'Adivina mi número'!")
    print("Estoy pensando en un número del 1 al 20.")
    print("Tienes 5 intentos para adivinarlo.")

    while intentos > 0:
        print("\nIntento restante:", intentos)
        a = int(input("Ingresa tu número: "))

        if a < nro:
            print("Mi número es mayor.")
        elif a > nro:
            print("Mi número es menor.")
        else:
            print("Adivinaste Mi número era", nro)
            return

        intentos -= 1

    print("\nNo adivinaste. Mi número era", nro)

adivinanro()
      