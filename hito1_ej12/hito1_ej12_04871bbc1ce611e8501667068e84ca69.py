#Juego adivina mi número
import random
numero = random.randrange(1,20)
print("Juguemos a adivinar el número, se asignará un número aleatoriamente con rango de 1 al 20, ingrese un número para adivinarlo,"
"¡SUERTE!")

n = eval(input("primer intento: "))
if n == numero:
    print("ADIVINASTE!!, mi número era",numero)
else:
    if n < numero:
        print("Mi número es mayor")
    else:
        if n > numero:
            print("Mi número es menor")

    a = int(input("segundo intento: "))
    if a == numero:
        print("ADIVINASTE!!, mi número era: ",numero)
    else:
        if a < numero:
            print("Mi número es mayor")
        else:
            if a > numero:
                print("Mi número es menor")

        b = int(input("tercer intento: "))
        if b == numero:
            print("ADIVINASTE!!, mi número era", numero)
        else:
            if b < numero:
                print("Mi número es mayor")
            else:
                if b > numero:
                    print("Mi número es menor")

            z = int(input("cuarto intento:"))
            if z == numero:
                print("ADIVINASTE!!, mi numero era:",numero)
            else:
                if z < numero:
                    print("mi numero es mayor")
                else:
                    if z > numero:
                        print("mi numero es menor")

                y= int(input("ultima oportunidad:"))
                if y == numero:
                    print("ADIVINASTE!!, mi numero era:",numero)
                else:
                    print("no adivinaste, mi numero era:",numero)      