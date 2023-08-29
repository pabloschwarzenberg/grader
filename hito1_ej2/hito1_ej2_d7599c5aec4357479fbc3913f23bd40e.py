#Contestador de celular
tele = input("Ingrese número telefónico: ")
hr = int(input("Ingrese hora de la llamada: "))
h1 = int(tele[5:8])
h2 = int(tele[0:3])
if 0 <= hr <= 7:
    print("CONTESTAR")
elif 7 < hr < 14 and h1 == 909:
    print("CONTESTAR")
elif 17 <= hr <= 19 and h2 != 877:
    print("CONTESTAR")
else:
    if 17 <= hr <= 19 and h2 == 877:
        print("NO CONTESTAR")
    elif hr >19:
        print("NO CONTESTAR")
    elif 14 <= hr <17:
        print("NO CONTESTAR")
    else:
        print("NO CONTESTAR")   