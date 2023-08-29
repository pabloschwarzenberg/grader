#Contestador de celular
ND=int(input("ingrese numero telefonico",))
hora=int(input("ingrese hora de llamada (0 a 23 horas)",))
NF=ND%1000
inicio=ND//100000
if(hora<=0 and hora<=7):
    print("CONTESTAR")
if(hora>7 and hora<=14):
    if(NF==909):
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
if(hora>=17 and hora<=19):
    if(inicio==877):
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
if(hora>19):
    print("NO CONTESTAR")