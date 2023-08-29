saldocajero=1000000
saldocuenta=100000
i=1
f=1
while i<4:
    if f==1:
        u=input("ingrese usuario: ")
        c=input("ingrese clave: ")
        if u==str(10334151) and c==str(1803):
            a=int(input("¿cual es el monto a retirar?: "))
            if a<=saldocuenta:
                saldocuenta =saldocuenta - a
                saldocajero =saldocajero - a
                print("saldo cuenta=", str(saldocuenta))
                print("saldo cajero=", str(saldocajero))
                break
            else:
                print("monto no permitido")
                break
        else:
            print("clave invalida")
            i=i+1
    print("tarjeta bloqueada")
