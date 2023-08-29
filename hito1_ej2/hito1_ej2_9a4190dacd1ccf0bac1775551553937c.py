numero=int(input("ingrese numero de 8 digitos: "))
hora=int(input("ingrese hora entre 0 y23: "))
com=int(numero/87700000)
if hora>=0 and hora<=7:
    print("CONTESTAR")
if hora<14:
    if ((numero-909)%1000)==0:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
if 17<=hora<=19:
    if com>=1:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
if hora>19:
    print("NO CONTESTAR") 