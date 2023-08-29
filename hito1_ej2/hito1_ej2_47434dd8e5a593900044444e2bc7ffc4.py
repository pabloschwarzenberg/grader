#Contestador de celular
T=str(input("Ingrese numero telefonico: "))
H=int(input("Ingrese hora: "))
T1=int(T[:3])
T2=int(T[5:])
if 0<=H<=7:
    print("CONTESTAR")
if 7<H<=14:
    if T2==909:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
if 14<H<17:
    print("NO CONTESTAR")
if 17<=H<=19:
    if T1==877:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
if H>19:
    print("NO CONTESTAR")      