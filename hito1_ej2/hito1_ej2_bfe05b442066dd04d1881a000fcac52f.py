numero=int(input("Ingrese numero telefonico (8 dígitos):"))
hora=int(input("Ingrese hora (0 a 23):"))

NT_txt=str(numero)

if hora>=0 and hora<=7:
    print("CONTESTAR")
elif hora<=14 and NT_txt.find("909")==5:
        print("CONTESTAR")
elif hora>=17 and hora<=19:
    if NT_txt.find("877")==0:
        print("NO CONTESTAR")
    else: print("CONTESTAR")
else:
    print("NO CONTESTAR") 