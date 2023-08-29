usuario=int(input("Ingrese usuario: "))
while usuario != 10334151:
    usuario = int(input("ERROR, Ingrese usuario: "))

clave=int(input("Ingrese clave: "))
intentos= 0
while clave != 1803:
    intentos=intentos+1
    if intentos==3:
        print("Tarjeta bloqueada")
        break
    else:
        clave = int(input("Clave invalida: "))
saldo_cajero=1000000
saldo_cuenta=100000
if intentos !=3:
    respuesta="S"
    while respuesta=="S":
        monto_retirar=int(input("Ingrese su monto: "))
        if monto_retirar<= saldo_cajero:
            if monto_retirar<=saldo_cuenta:
                saldo_cajero=saldo_cajero-monto_retirar
                saldo_cuenta=saldo_cuenta-monto_retirar
                print("saldo cuenta=",saldo_cuenta)
                print("saldo cajero=",saldo_cajero)
            else:
                print("monto no permitido")
        else:
            print("monto no permitido")
        respuesta=input("Quiere volver a operar(S/N): ")