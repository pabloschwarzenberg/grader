#Juego adivina mi número
import random
intentos = 0

numero = random.randint(1,20)

def Adivinador(l):
    if l == numero:
        print("adivinaste mi numero era",numero)
        b = 1
        return b
    elif l < numero:
        print("Mi nuero es mayor")
        return numero
    elif l > numero:
        print("Mi numero es menor")
        return numero

b = 0
while b == 0:
    if intentos == 5:
        print("turnos agotados")
        break
    else:
        print("Ingresa un numero")
        p = input()
        if p == numero:
            print ("adivinaste mi numero era",numero)
            break
        elif p != numero:
            intentos += 1
            Adivinador(int(p))
        