#Cajero Automático
while True:
    intentos=0
    while intentos<3:
        usuario=input("intruzca usuario ")
        clave=input("introduzca clave")
        if usuario=="10334151" and  clave=="1803":
            print("Clave exitosa")
            break 
        else: 
            print("clave o usuario incorrecto")
            intentos=intentos+1
    if intentos==3:
        print("tarjeta bloqueada")
    else:
        saldo_cuenta=100000
        saldo_cajero=1000000
        monto=int(input("introduzca monto a retirar"))
        if saldo_cuenta<monto:
            print("monto no permitido")
        elif saldo_cuenta==monto:
            print("monto permitido")
            saldo_cuenta=saldo_cuenta-monto
            saldo_cajero=saldo_cajero-monto
            print("saldo cuenta=",saldo_cuenta)
            print("saldo cajero=",saldo_cajero)  

            break
        else:
            print("monto permitido")
            saldo_cuenta=saldo_cuenta-monto
            saldo_cajero=saldo_cajero-monto
            print("saldo cuenta=",saldo_cuenta)
            print("saldo cajero=",saldo_cajero)
            break
        