#Cajero Automático
saldocajero=1000000
usuario=10334151
clave="1803"
saldocuenta=100000
cont=1
usu=input("ingrese usuario:")
if int(usu)==usuario:
    while True:
        if cont>3:
            print("tarjeta bloqueada")
            break
        contra=input()
        while True:
            if contra!="N":
                break
        if contra!=clave:
            print("clave invalida")
            cont+=1
        else:
            monto=int(input("ingrese monto a retirar:"))
            if monto<saldocuenta and monto<saldocajero:
                saldocajero=saldocajero-monto
                saldocuenta=saldocuenta-monto
                print("saldo cuenta=",saldocuenta)
                print("saldo cajero=",saldocajero)
            else:
                print("monto no permitido")


          