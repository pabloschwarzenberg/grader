#Contestador de celular
numero=int(input("Ingrese numero telefonico: "))
hora=int(input("Ingrese hora: "))
if (hora <= 7) and (hora >= 0):
    print("CONTESTAR")
if hora >7 and hora <= 14:
    if ((numero-909)%1000==0):
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
if hora >= 17 and hora <= 19:
    if ((numero-877)%1000==0):
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
if hora >= 18 or (hora >14 and hora < 17):
    print("NO CONTESTAR")