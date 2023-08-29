from random import randint
intentosRealizados = 0
print("Hola, ¿cómo te llamas? ")
nombre=input()
numero = randint(1,20)
print("Bueno, " + nombre + ", estoy pensando un número entre el 1 y el 20.")
while intentosRealizados < 5:
    print("Intenta adivinar: ")
    estimacion = int(input())
    try:

        if estimacion < numero:
            print("¡Tu número es muy bajo! ")
        elif estimacion > numero:
            print("¡Tu número es muy alto! ")
        else:
            print("Adivinaste, mi nùmero era"+str(numero))
            break
        intentosRealizados += 1
        estimacion = 0
    except ValueError:
            print("Ingrese solo números")

if intentosRealizados == 5:
    print("Lo siento. El número era " + str(numero))
from random import randint
intentosRealizados = 0
print("Hola, ¿cómo te llamas? ")
nombre=input()
numero = randint(1,20)

print("Bueno, " + nombre + ", estoy pensando un número entre el 1 y el 20.")
while intentosRealizados < 5:
    estimacion = int(input("Intenta adivinar: "))
    try:

        if estimacion < numero:
            print("¡Tu número es muy bajo! ")
        elif estimacion > numero:
            print("¡Tu número es muy alto! ")
        else:
            print("Adivinaste, mi nùmero era "+str(numero))
            break
        intentosRealizados += 1
        estimacion = 0
    except ValueError:
            print("Ingrese solo números")

if intentosRealizados == 5:
    print("No adivinaste, mi nùmero era " + str(numero))
    
from random import randint
intentosRealizados = 0

numero = randint(1,20)

print("Bueno, estoy pensando un número entre el 1 y el 20.")
while intentosRealizados < 5:
    estimacion = int(input("Intenta adivinar: "))
    if 0<=estimacion<=20:

        if estimacion < numero:
            print("¡Tu número es muy bajo! ")
        elif estimacion > numero:
            print("¡Tu número es muy alto! ")
        else:
            print("Adivinaste, mi nùmero era "+str(numero))
            break
        intentosRealizados += 1
        estimacion = 0
    else:
        print("Ingrese solo números")

if intentosRealizados == 5:
    print("No adivinaste, mi nùmero era " + str(numero))