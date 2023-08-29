#Cajero Automático
intentos=3
saldo_cuenta=100000
saldo_cajero=1000000

usuario=int(input("numero de usuario"))
if usuario==10334151:
    while intentos>0:
        clave_tarjeta=int(input("ingrese su clave"))
        if clave_tarjeta!=1803:
            print("clave invalida")
            intentos=intentos-1
        else:
            print(saldo_cuenta)
            monto_retirar=int(input("monto a retirar:"))
            if monto_retirar>saldo_cuenta:
                print("Monto no permitido")
            else:
                print("saldo cuenta=",(saldo_cuenta)-(monto_retirar),"saldo cajero=",(saldo_cajero)-(monto_retirar))
            break
else:
    print("usuario no encontrado")
