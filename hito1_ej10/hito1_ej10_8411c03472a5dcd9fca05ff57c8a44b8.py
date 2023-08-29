#Cajero Automático
saldo_inicial = 1000000
saldo_cajero = 1000000

def verificar_usuario():
    intentos = 0
    bloqueado = False

    while True:
        usuario = input("Ingrese su usuario: ")
        clave = input("Ingrese su clave: ")

        if usuario == "10334151" and clave == "1803":
            return True
        else:
            intentos += 1
            if intentos >= 3:
                bloqueado = True
                break
            print("Clave inválida. Intente nuevamente.")

    if bloqueado:
        print("Tarjeta bloqueada. Contacte al banco.")
        return False

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
        print("Retiro exitoso.")
        print("Saldo cuenta =", saldo_cuenta)
        print("Saldo cajero =", saldo_cajero)
        return saldo_cuenta, saldo_cajero

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

