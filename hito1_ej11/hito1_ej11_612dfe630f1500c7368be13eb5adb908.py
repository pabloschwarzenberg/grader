saldo_cajero=1000000
saldo_cuenta=100000
bi20mil=20000
bi10mil=10000
bi5mil=5000
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
                retira20mil=0
                retira10mil = 0
                retira5mil = 0
                saldo_cajero = saldo_cajero - monto_retirar
                saldo_cuenta = saldo_cuenta - monto_retirar
                while(monto_retirar>0):
                    if (monto_retirar>=20000 and bi20mil>0):
                        retira20mil=retira20mil+1
                        bi20mil=bi20mil-1
                        monto_retirar=monto_retirar-20000
                    if monto_retirar>=10000 and bi10mil>0:
                        retira10mil = retira10mil + 1
                        bi10mil = bi10mil - 1
                        monto_retirar = monto_retirar - 10000

                    if monto_retirar>=5000 and bi5mil>0:
                        retira5mil = retira5mil + 1
                        bi5mil = bi5mil - 1
                        monto_retirar = monto_retirar - 5000



                saldo_cajero=saldo_cajero-monto_retirar
                saldo_cuenta=saldo_cuenta-monto_retirar
                print("saldo cuenta=",saldo_cuenta)
                print("saldo cajero=",saldo_cajero)
                print("billetes 20000=",retira20mil)
                print("billetes 10000=",retira10mil)
                print("billetes 5000=", retira5mil)

            else:
                print("monto no permitido")
        else:
            print("monto no permitido")
        respuesta=input("Quiere volver a operar(S/N): ")