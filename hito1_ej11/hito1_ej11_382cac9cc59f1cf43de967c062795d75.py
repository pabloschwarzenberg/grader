import sys

saldo_cajero=1000000
saldo_cuenta=100000
usuario="10334151"
clave="1803"
salir="N"
billetes20000=20
billetes10000=40
billetes5000=40

while salir=="N":
    u=input("Ingrese usuario: ")
    contador=0
    while contador<3:
        c=input("Ingrese clave: ")
        if c!=clave:
            print("clave invalida")
            contador=contador+1
        else:
            break
    if contador==3:
        print("tarjeta bloqueada")
        sys.exit(1)
    monto=int(input("Ingresa el monto a retirar: "))
    if monto>saldo_cajero or monto>saldo_cuenta:
        print("monto no permitido")
    else:
        saldo_cajero=saldo_cajero-monto
        saldo_cuenta=saldo_cuenta-monto
        print("Saldo cuenta=",saldo_cuenta)
        print("Saldo Cajero=",saldo_cajero)
        entrega20000=0
        entrega10000=0
        entrega5000=0
        if monto>=20000:
            entrega20000=monto//20000
            if entrega20000>billetes20000:
                entrega20000=billetes20000
            monto=monto-entrega20000*20000
        if monto>=10000:
            entrega10000=monto//10000
            if entrega10000>billetes10000:
                entrega10000=billetes10000
            monto=monto-entrega10000*10000
        if monto>=5000:
            entrega5000=monto//5000
            if entrega5000>billetes5000:
                entrega5000=billetes5000
            monto=monto-entrega5000*5000
        if monto>0:
            print("monto no entregable")
        else:
            print("Billetes 20000=",entrega20000)
            print("Billetes 10000=",entrega10000)
            print("Billetes 5000=",entrega5000)

    salir=input("Deseas salir?")

      