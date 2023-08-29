
import math
TL = int(input("ingrese numero telefonico :"))
HR = int(input("ingrese hora :"))
TLS = str(TL)
TLS_2 = TLS[5:8]
TLS_3 = TLS[0:3]
if math.log10(TL)<=8:
    if HR>=0 and HR <=23:
        if (HR>=0 and HR<=7) or (HR<=14 and TLS_2 == "909") or (HR>=17 and HR<=19 and TLS_3 != "877"):
            print("CONTESTAR")
        else:
            print("NO CONTESTAR")
    else:
        print("hora invalida")
        
else:
    print("numero de telefono invalido")
    