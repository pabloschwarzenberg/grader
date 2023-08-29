import random
intentos = 0

numero = random.randint(1,20)

def Adivinador(n):
    if n == numero:
        print("adivinaste mi numero era",numero)
        b = 1
        return b
    elif n < numero:
        print("Mi nuero es mayor")
        return numero
    elif n > numero:
        print("Mi numero es menor")
        return numero

if __name__ == "__main__":
    pass
         