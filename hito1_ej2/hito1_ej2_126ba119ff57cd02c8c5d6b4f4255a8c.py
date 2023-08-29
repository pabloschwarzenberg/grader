#Contestador de celular
numero=int(input("Ingrese numero celular: "))
hora=int(input("Ingrese hora: "))
if hora>=0 and hora<=7:
    print("CONTESTAR")
elif hora>7 and hora<14:
    if (numero%1000)==909:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif hora>=14 and hora<17:
    print("NO CONTESTAR")
elif hora>=17 and hora<=19:
    if (numero//1000000)==877:
        print("NO CONTESTAR")
    else:
        print("NO CONTESTAR")
elif hora>19 and hora <=23:
    print("NO CONTESTAR")