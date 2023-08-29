numero=int(input("ingresa un numero de 8 cifras: "))
hora=int(input("ingresa la hora de la llamada: "))
if hora>=0 and hora<=7:
    print("CONTESTAR")
elif hora>7 and hora<14:
    if str(numero).endswith("909"):
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif hora>14 and hora<17:
    print("NO CONTESTAR")
elif hora>=17 and hora<=19:
    print("CONTESTAR")
    if str(numero).startswith("877"):
        print("NO CONTESTAR")
elif hora>19 and hora<23:
    print("NO CONTESTAR")