#Cajero Automático
salir="N"
while salir=="N":
    intentos=3
    saldocajero=1000000
    while(intentos>0):
        U=input("Igrese Su Usuario")
        K=input("Ingrese Su Clave")
        if(U=="10334151") and (K=="1803"):
            print("Acceso Consedido")
            saldousuario1=100000
            R=input("Ingrese Cantidad a Retirar")
            R=int(R)
            if(int(R)>100000):
                print("Monto No Permitido")
                break
            elif(int(int(R)<100000 and int(R)>0)):
                saldocajero=int(saldocajero-R)
                saldousuario1=int(saldousuario1-R)
                print("saldo cajero=",saldocajero)
                print("saldo cuenta=",saldousuario1)
                break
        else:
            print("clave invalida")
            intentos=intentos-1
    if intentos==0:
        print("Tarjeta Bloqueada")
    salir=input("Quieres Salir")
      