#Contestador de celular
quit=0
NC="NO CONTESTAR"
C="CONTESTAR"
while(quit!=1):
    telefono=int(input("Ingrese numero telefonico:"))
    if(len(str(telefono))!=8):
        print("Número inválido, intente denuevo.")
        continue
    else:
        #print("TEST:",str(telefono)[-3:-1])
        #print("TEST:",str(telefono)[-3:])
        pass
    while(quit!=1):
        hora=int(input("Ingrese hora de la llamada:"))
        if(hora>=0 and hora<=23):
            quit=1
        else:
            print("Hora inválida, intente denuevo.")
            continue
if(hora >=0 and hora<=7):
    print(C)
elif(hora >=8 and hora<=14 and str(telefono)[-3:]!="909"):
    print(NC)
elif(hora >=8 and hora<=14 and str(telefono)[-3:]=="909"):
    print(C)
elif(hora >= 17 and hora<=19 and str(telefono)[:3]!="877"):
    print(C)
elif(hora >= 17 and hora<=19 and str(telefono)[:3]=="877"):
    print(NC)
else:
    print(NC)