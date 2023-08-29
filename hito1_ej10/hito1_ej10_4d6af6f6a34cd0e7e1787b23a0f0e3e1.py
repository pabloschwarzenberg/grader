#Cajero Automático
import sys 

usuario=int(input("Ingrese usuario:"))
clave=int(input("Ingrese clave:"))

saldocajero=1000000
salocuenta=100000


if usuario==10334151 and clave==1803:
    monto=int(input("Monto a retirar:"))
    if monto<100000:
        saldocuenta=100000-monto
        saldocajero=1000000-monto

        print("saldo cuenta=",saldocuenta)
        print("saldo cajero=",saldocajero)

    elif monto>10000:
         print("monto no permitido")
##
if usuario==10334151 and clave!=1803:
    print("clave invalida")
    clave=int(input("Ingrese clave:"))
    if clave==1803:
        monto=int(input("Monto a retirar:"))
        if monto<100000:
            saldocuenta=100000-monto
            saldocajero=1000000-monto

            print("saldo cuenta=",saldocuenta)
            print("saldo cajero=",saldocajero)
    
    elif monto>10000:
         print("monto no permitido")
        

if clave!=1803:
    print("clave invalida")
    clave=int(input("Ingrese clave:"))
    if clave==1803:
        monto=int(input("Monto a retirar:"))
        if monto<100000:
            saldocuenta=100000-monto
            saldocajero=1000000-monto

            print("saldo cuenta=",saldocuenta)
            print("saldo cajero=",saldocajero)
    
    elif monto>10000:
         print("monto no permitido")

if clave!=1803:
   print("tarjeta bloqueada")
   sys.exit(0)

              