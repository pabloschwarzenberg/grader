#Contestador de celular
tl = int(input("Ingrese numero telefonico: "))
hr = int(input("Ingrese hora de la llamada: "))

tl1 = (tl%1000)
tl2 = (tl//100000)


if hr <= 7 and hr >= 0:
    print("CONTESTAR")
elif hr < 14:
    if tl1 == 909:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif hr >= 17 and hr <= 19:
    if tl2 == 877:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
else:
    print("NO CONTESTAR")
