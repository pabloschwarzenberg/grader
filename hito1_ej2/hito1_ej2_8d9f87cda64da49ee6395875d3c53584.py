#Contestador de celular
NT = str(int(input("Ingrese número telefónico de 8 cifras:")))
hora = int(input("Ingrese la hora de 0 a 23:"))
extraer1 = NT[0:3]
extraer2 = NT[5:8]
f = str("909")
i = str("877")
if (hora<14):
    if (extraer2==f):
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
else:
    if (17<=hora<=19):
        if (extraer1==i):
            print("NO CONTESTAR")
        else:
            print("CONTESTAR")
    else:
        if (hora>19):
            print("NO CONTESTAR")
        else:
            if (0<=hora<=7):
                print("CONTESTAR")      