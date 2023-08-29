#Juego adivina mi número
import random
intentos = 0

numero = random.randint(1,20)

def Adivinador(n):
    if n == numero:
        print("adivinaste mi numero era",numero)
        c = 1
        return c
    elif n < numero:
        print("Mi nuero es mayor")
        return numero
    elif n > numero:
        print("Mi numero es menor")
        return numero

c = 0
while c == 0:
    if intentos == 5:
        print("turnos agotados")
        break
    else:
        print("Ingresa un numero")
        x = input()
        if x == numero:
            print ("adivinaste mi numero era",numero)
            break
        elif x != numero:
            intentos += 1
            Adivinador(int(x))