#Contestador de celular
NF = int(input("indique numero de telefono de 8 cifras: "))
Hr = float(input("indique hora de la llamada: "))
if Hr >= 0 and Hr <= 7:
    print("CONTESTAR")
elif Hr > 7 and Hr <= 14:
    if NF %1000 == 909:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif Hr >= 17 and Hr <= 19:
    if NF //100000 == 877:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
else:
    print("NO CONTESTAR")      