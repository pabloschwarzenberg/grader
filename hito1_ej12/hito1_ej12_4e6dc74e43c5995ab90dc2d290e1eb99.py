#Juego adivina mi número
# Selecciona numero del 1 al 20

from random import randrange

a = randrange(20)
x = 1

#intento de adivinar el numero
while x <= 5:
    b = input("Intente adivinar mi numero: ")
    print("~"*30)
    try:
        b = int(b)
        if b > a:
            print("Tu numero es mayor al que estoy pensando.")
            print("~"*30)
            x = x + 1
        elif b < a:
            print("Tu numero es menor al que estoy pensando.")
            print("~"*30)
            x = x + 1
        elif b == a:
            print("Adivinaste, mi numero era ", a)
            print("~"*30)
            exit()
    except ValueError:
        print("Eso no es un numero.")
        print("~"*30)

print("Intentos acabados.")
print("Mi numero era ", a)
print("~"*30)