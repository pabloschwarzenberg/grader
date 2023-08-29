#Juego adivina mi número
import random
num = random.randrange(1,20)
print("Juguemos a adivinar el número, se asignará un número aleatoriamente con rango de 1 al 20, ingrese un número para adivinarlo,"
      "Tienes solamente 5 intentos, ¡SUERTE!")
x = eval(input("Ingrese número: "))
if x == num:
    print("Adivinaste, mi número era",num)
else:
    if x<num:
        print("Mi número es mayor")
    else:
        if x>num:
            print("Mi número es menor")

    a=int(input("Ingrese número: "))
    if a == num:
        print("Adivinaste, mi número era: ",num)
    else:
        if a < num:
            print("Mi número es mayor")
        else:
            if a > num:
                print("Mi número es menor")

    b = int(input("Ingrese número: "))
    if b == num:
        print("FELICIDADES, adivinaste, mi número era", num)
    else:
        if b < num:
            print("Mi número es mayor")
        else:
            if b > num:
                print("Mi número es menor")
    z = int(input("Ingrese número: "))
    if z == num:
        print("FELICIDADES, adivinaste, mi número era", num)
    else:
        if z < num:
            print("Mi número es mayor")
        else:
            if z > num:
                print("Mi número es menor")
    f = int(input("Ingrese número: "))
    if f == num:
        print("FELICIDADES, adivinaste, mi número era: ", num)
    else:
        if f < num:
            print("Mi número es mayor")
        else:
            if f > num:
                print("Mi número es menor")

    if f!= num:
        print("No adivinaste, mi número era: ",num)
