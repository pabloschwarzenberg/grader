#Cajero Automático
billetes_20000 = 20
billetes_10000 = 40
billetes_5000 = 40

def realizar_retiro(saldo_cuenta, saldo_cajero):
    if saldo_cuenta <= 0:
        print("Saldo insuficiente. No se puede realizar retiros.")
        return saldo_cuenta, saldo_cajero

    monto = float(input("Ingrese el monto a retirar: "))

    if monto <= 0:
        print("Monto no permitido. Intente nuevamente.")
        return saldo_cuenta, saldo_cajero
    elif monto > saldo_cuenta or monto > saldo_cajero:
        print("Saldo insuficiente. No se puede realizar el retiro.")
        return saldo_cuenta, saldo_cajero
    else:
        saldo_cuenta -= monto
        saldo_cajero -= monto

        billetes_20000_entregados = min(monto // 20000, billetes_20000)
        monto -= billetes_20000_entregados * 20000

        billetes_10000_entregados = min(monto // 10000, billetes_10000)
        monto -= billetes_10000_entregados * 10000

        billetes_5000_entregados = min(monto // 5000, billetes_5000)
        monto -= billetes_5000_entregados * 5000

        print("Retiro exitoso.")
        print("Saldo cuenta =", saldo_cuenta)
        print("Saldo cajero =", saldo_cajero)
        print("Billetes 20000 =", int(billetes_20000_entregados))
        print("Billetes 10000 =", int(billetes_10000_entregados))
        print("Billetes 5000 =", int(billetes_5000_entregados))

        return saldo_cuenta, saldo_cajero

def verificar_usuario():
    usuario = input("Ingrese el usuario: ")
    clave = input("Ingrese la clave: ")

    if usuario == "10334151" and clave == "1803":
        return True
    else:
        print("Clave inválida.")
        return False

def cajero_automatico():
    saldo_cuenta = 100000
    saldo_cajero = 1000000

    if verificar_usuario():
        saldo_cuenta, saldo_cajero = realizar_retiro(saldo_cuenta, saldo_cajero)
        while True:
            respuesta = input("¿Desea realizar otra transacción? (S/N): ")
            if respuesta.upper() != "S":
                break
            saldo_cuenta, saldo_cajero = realizar_retiro(saldo_cuenta, saldo_cajero)

cajero_automatico()
