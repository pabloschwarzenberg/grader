from random import randint
a=randint(1,20)
#primer intento
P = int(input("¿cual numero crees que es?, (tienes 5 intentos): "))
if P == a:
    print("Muy bien, lo has logrado")
else:
    print("error, intentalo otra vez")
    if P > a:
        print("el numero que ingresaste es mayor al numero secreto")
    else:
        print("el numero que ingresaste es menor al numero secreto")
#segundo intento
P = int(input("¿cual numero crees que es?, (tienes 4 intentos): "))
if P == a:
    print("Muy bien, lo has logrado")
else:
    print("error, intentalo otra vez")
    if P > a:
        print("el numero que ingresaste es mayor al numero secreto")
    else:
        print("el numero que ingresaste es menor al numero secreto")
#tercer intento
P = int(input("¿cual numero crees que es?, (tienes 3 intentos): "))
if P == a:
    print("Muy bien, lo has logrado")
else:
    print("error, intentalo otra vez")
    if P > a:
        print("el numero que ingresaste es mayor al numero secreto")
    else:
        print("el numero que ingresaste es menor al numero secreto")
#cuarto intento
P = int(input("¿cual numero crees que es?, (tienes 2 intentos): "))
if P == a:
    print("Muy bien, lo has logrado")
else:
    print("error, intentalo otra vez")
    if P > a:
        print("el numero que ingresaste es mayor al numero secreto")
    else:
        print("el numero que ingresaste es menor al numero secreto")
#quinto y ultimo intento
P = int(input("¿cual numero crees que es?, (tienes 1 intento): "))
if P == a:
    print("Muy bien, lo has logrado")
else:
    print("error, intentalo otra vez")
    if P > a:
        print("el numero que ingresaste es mayor al numero secreto")
    else:
        print("el numero que ingresaste es menor al numero secreto")