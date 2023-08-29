#Contestador de celular
numero=int(input("Ingrese numero telefonico: "))
hora=int(input("Ingrese la hora de la llamada: "))
if hora>=0 and hora<=7:
    print("CONTESTAR")
elif hora>=8 and hora<=14:
    dosa=float((numero-909)/1000)
    dosb=int((numero-909)/1000)
    if dosa==dosb:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif hora==15 or hora==16:
    print("NO CONTESTAR")
elif hora>=17 and hora<=19:
    if 87700000<=numero and numero<=87799999:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
elif hora>=19 and hora<=23:
    print("NO CONTESTAR")