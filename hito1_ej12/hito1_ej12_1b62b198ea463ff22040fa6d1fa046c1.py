#Juego adivina mi número
import random

x =(random.randint(1, 20))

print("bienvenido a este juego de adivinanza")
print()
print("tienes 5 intentos para adividar el numero")
print()
print("el numero es que tienes que adividar su intervalo es del 1 al 20")
print()
print("suerte")
print()
print("primer intento")

y = int(input("1:"))
if x==y:
    print("Adivinaste, mi número era ",x)
else:
    if x<y:
        print("mi numero es menor")
    else:
        print("mi numero es mayor")
    y = int(input("2:"))
    if x==y:
        print("Adivinaste, mi número era ",x)
    else:
        if x<y:
           print("mi numero es menor")
        else:
           print("mi numero es mayor")
        y = int(input("3:"))
        if x==y:
            print("Adivinaste, mi número era ",x)
        else:
            if x<y:
                print("mi numero es menor")
            else:
                print("mi numero es mayor")
            y = int(input("4:"))
            if x==y:
                print("Adivinaste, mi número era ",x)
            else:
                if x<y:
                    print("mi numero es menor")
                else:
                    print("mi numero es mayor")
                y = int(input("ultimo intento:"))
                if x==y:
                    print("Adivinaste, mi número era ",x)
                else:
                    if x<y:
                        print("mi numero es menor")
                    else:
                        print("mi numero es mayor")
                    print("No adivinaste, mi número era ", x)