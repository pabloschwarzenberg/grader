#Juego adivina mi número
import random
x = random.randrange(1,20)
print("Juguemos a adivinar el número, mi numero estara entre 1-20, ingrese un número para adivinarlo,"
      "Tienes solamente 5 intentos")
valor = eval(input("Ingrese número: "))
if (valor == x):
    print("Adivinaste, mi número era",x)
else:
    if (valor<x):
        print("Mi número es mayor")
    else:
        if (valor>x):
            print("Mi número es menor")

    valor1=int(input("Ingrese número: "))
    if (valor1 == x):
        print("Adivinaste, mi número era: ",x)
    else:
        if (valor1 < x):
            print("Mi número es mayor")
        else:
            if (valor1 > x):
                print("Mi número es menor")

    valor2 = int(input("Ingrese número: "))
    if (valor2 == x):
        print("FELICIDADES, adivinaste, mi número era", x)
    else:
        if (valor2 < x):
            print("Mi número es mayor")
        else:
            if (valor2 > x):
                print("Mi número es menor")
    valor3 = int(input("Ingrese número: "))
    if (valor3 == x):
        print("FELICIDADES, adivinaste, mi número era", x)
    else:
        if (valor3 < x):
            print("Mi número es mayor")
        else:
            if (valor3 > x):
                print("Mi número es menor")
    valor4 = int(input("Ingrese número: "))
    if (valor4 == x):
        print("FELICIDADES, adivinaste, mi número era: ", x)
    else:
        if (valor4 < x):
            print("Mi número es mayor")
        else:
            if (valor4 > x):
                print("Mi número es menor")

    if (valor4!= x):
        print("No adivinaste, mi número era",x)