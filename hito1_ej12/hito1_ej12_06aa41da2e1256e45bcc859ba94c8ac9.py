import random

class AdivinaMiNumero:
    def __init__(self):
        self.numero_secreto = random.randint(1, 20)
        self.intentos = 0

    def jugar(self):
        print("¡Bienvenido a 'Adivina mi número'!")
        print("Tienes 5 intentos para adivinar el número secreto.")
        print("El número está entre 1 y 20.")

        while self.intentos < 5:
            numero = int(input("Ingresa un número: "))

            if numero == self.numero_secreto:
                print("¡Adivinaste! Mi número era {0}.".format(self.numero_secreto))
                return

            if numero < self.numero_secreto:
                print("Mi número es mayor.")
            else:
                print("Mi número es menor.")

            self.intentos += 1
            print("Te quedan {0} intentos.".format(5 - self.intentos))

        print("No adivinaste. Mi número era {0}.".format(self.numero_secreto))


if __name__ == "__main__":
    juego = AdivinaMiNumero()
    juego.jugar()
