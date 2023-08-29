#Contestador de celular
NT=int(input("Ingrese numero telefonico (8 dígitos):"))
H=int(input("Ingrese hora (0 a 23):"))

NT_txt=str(NT)

if H>=0 and H<=7:
    print("CONTESTAR")
elif H<=14 and NT_txt.find("909")==5:
        print("CONTESTAR")
elif H>=17 and H<=19:
    if NT_txt.find("877")==0:
        print("NO CONTESTAR")
    else: print("CONTESTAR")
else:
    print("NO CONTESTAR")      