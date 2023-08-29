#Contestador de celular
numerotelefonico=int(input("su numero telefonico: "))
hora=int(input("Ingrese su hora: "))
if hora>=0 and hora<=7:
    print("CONTESTAR")
elif hora>7 and hora<14:
    if (numerotelefonico%1000)==909:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif hora>=14 and hora<17:
    print("NO CONTESTAR")
elif hora>=17 and hora<=19:
    if (numerotelefonico//1000000)==877:
        print("NO CONTESTAR")
    else:
        print("NO CONTESTAR")
elif hora>19 and hora <=23:
    print("NO CONTESTAR")     