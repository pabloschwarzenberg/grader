import random
input("¡Bienvenido a Adivina buen adivinador!, en este juego debes adivinar el número que tendrá el programa, el cuales un número entre 1 y 20. Si adivinas... ¡pasarás el ramo!. Presione enter para continuar...")
x= int(input("Ingrese el número que crea usted que es (tenga en cuenta que son 5 intentos): "))
c=(random.randrange(1, 20))
if x > c:
    print("Mi número es menor al que has introducido. Te quedan 4 intentos.")
elif x < c:
    print("Mi número es mayor al que has introducido. Te quedan 4 intentos.")
else:
    print("Adivinaste, mi número era: ", c)

if x > c:
    print("Mi número es menor al que has introducido. Te quedan 3 intentos.")
elif x < c:
        print("Mi número es mayor al que has introducido. Te quedan 3 intentos.")
else:
    print("Adivinaste, mi número era: ", c)

x= int(input("Introduzca otro número: "))

if x > c:
    print("Mi número es menor al que has introducido. Te quedan 2 intentos.")
elif x < c:
    print("Mi número es mayor al que has introducido. Te quedan 2 intentos.")
else:
    print("Adivinaste, mi número era: ", c)

x= int(input("Introduzca otro número: "))

if x > c:
        print("Mi número es menor al que has introducido. Te quedan 1 intentos.")
elif x < c:
        print("Mi número es mayor al que has introducido. Te quedan 1 intentos.")
else:
        print("Adivinaste, mi número era: ", c)
x= int(input("Introduzca otro número: "))
if x > c:
    print("No adivinaste, mi número era", c)
elif x < c:
    print("No adivinaste, mi número era", c)
else:
    print("Adivinaste, mi número era: ", c)
