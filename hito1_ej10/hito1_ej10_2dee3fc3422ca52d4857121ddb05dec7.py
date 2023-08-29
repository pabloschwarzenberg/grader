saldoi=1000000
intentos=3
while intentos>0:
    saldocuenta= 100000
    usuario = int(input("Ingrese usuario:"))
    clave = int(input("Ingrese clave:"))
    if usuario==10334151 and clave==1803:
        print("clave valida, Bienvenido")
        retiro=int(input("Ingrese monto a retirar:"))
        if (retiro<=saldocuenta):
            saldocuenta=saldocuenta-retiro
            saldocajero=saldoi-retiro
            print("saldo cuenta="+str(saldocuenta))
            print("saldo cajero="+str(saldocajero))
            break
    else:
        print("clave invalida")
        intentos=intentos-1
if intentos==0:
    print("tarjeta bloqueada")