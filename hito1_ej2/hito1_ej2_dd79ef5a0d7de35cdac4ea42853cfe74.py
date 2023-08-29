numero=int(input("Ingresar número de teléfono: "))
if numero<=10000000 and numero>=99999999:
    print("ERROR EN NÚMERO")
else:
    hora=int(input("Ingrese hora: "))
    firstnumb=(numero//100000)
    lastnumb=(numero%1000)
    
    if hora>=0 and hora<=7:
        print("CONTESTAR")
    elif hora<=14 and lastnumb==909:
        print("CONTESTAR")
    else:
        lastnumb!=877
        print("NO CONTESTAR")
