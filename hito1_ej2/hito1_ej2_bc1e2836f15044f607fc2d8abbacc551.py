#Contestador de celular
ntelefono=int(input("Ingrese numero telefonico:"))
horall=int(input("Ingrese hora de la llamada:"))
if horall>0 and horall<7:
    print("CONTESTAR")
else:
    if horall>7 and horall<14 and (str(ntelefono))[5:]=="909":
        print("CONTESTAR")
    else:
        if horall>17 and horall<19 and (str(ntelefono))[:2]=="877":
            print("CONTESTAR")
        else:
            print("NO CONTESTAR")