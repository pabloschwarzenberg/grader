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


monto=str(monto)
a=int(monto[-5])
b=a%2

e=int(monto[-4])
f=e%5
if b==0:
    c=int(a/2)
    print("billetes 20000=",c)

if b!=0:
    d=int(a/1)
    print("billetes 10000=",d)

if f==0:
    g=int(e/5)
    print("billetes 5000=",g)

    