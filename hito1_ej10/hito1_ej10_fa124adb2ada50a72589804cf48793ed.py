def verificar_clave(usuario, clave):
    if usuario == '10334151' and clave == '1803':
        return True
    return False

def retirar_dinero(saldo_cuenta, saldo_cajero):
    monto = 45000  

    if monto <= 0:
        print("Monto no permitido")
        return saldo_cuenta, saldo_cajero

    if monto > saldo_cuenta:
        print("Saldo insuficiente")
        return saldo_cuenta, saldo_cajero

    saldo_cuenta -= monto
    saldo_cajero -= monto

    print("saldo cuenta={0}".format(saldo_cuenta))
    print("saldo cajero={0}".format(saldo_cajero))

    return saldo_cuenta, saldo_cajero

def cajero():
    saldo_cuenta = 100000
    saldo_cajero = 1000000
    intentos = 0

    usuario = '10334151'  
    clave = '1803'  

    if verificar_clave(usuario, clave):
        intentos = 0
        saldo_cuenta, saldo_cajero = retirar_dinero(saldo_cuenta, saldo_cajero)
    else:
        intentos += 1
        print("Clave inválida")

        if intentos == 3:
            print("Tarjeta bloqueada")

    opcion = 'N'  

    if opcion.upper() == "N":
        return

cajero()