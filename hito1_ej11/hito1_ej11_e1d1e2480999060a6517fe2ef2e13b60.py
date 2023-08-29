def realizar_retiro(saldo_cuenta, saldo_cajero):
    clave_correcta = False
    intentos = 0

    while not clave_correcta:
        usuario = input("Ingrese su usuario: ")
        clave = input("Ingrese su clave: ")
        #usuario = 10334151
        #clave = 1803

        if usuario == "10334151" and clave == "1803":
            clave_correcta = True
        else:
            intentos += 1
            if intentos == 3:
                print("Tarjeta bloqueada")
                return saldo_cuenta, saldo_cajero
            print("Clave inválida. Intentos restantes:", 3 - intentos)

    monto_retiro = int(input("Ingrese el monto a retirar: "))
    
    saldo_cuenta -= monto_retiro
    print("saldo cuenta=", saldo_cuenta, sep="")

    if monto_retiro % 5000 != 0:
        print("Monto no permitido")
        return saldo_cuenta, saldo_cajero

    if monto_retiro > saldo_cuenta:
        print("Saldo insuficiente")
        return saldo_cuenta, saldo_cajero

    # Distribución de billetes
    billetes_20000 = min(monto_retiro // 20000, saldo_cajero // 20000)
    monto_retiro -= billetes_20000 * 20000
    saldo_cajero -= billetes_20000 * 20000

    billetes_10000 = min(monto_retiro // 10000, saldo_cajero // 10000)
    monto_retiro -= billetes_10000 * 10000
    saldo_cajero -= billetes_10000 * 10000

    billetes_5000 = min(monto_retiro // 5000, saldo_cajero // 5000)
    monto_retiro -= billetes_5000 * 5000
    saldo_cajero -= billetes_5000 * 5000

    if monto_retiro > 0:
        print("No hay suficientes billetes para el monto solicitado")
        return saldo_cuenta, saldo_cajero

    print("saldo cajero=", saldo_cajero, sep="")
    print("billetes 20000=", billetes_20000, sep="")
    print("billetes 10000=", billetes_10000, sep="")
    print("billetes 5000=", billetes_5000, sep="")

    return saldo_cuenta, saldo_cajero

saldo_cuenta = 100000
saldo_cajero = 1000000

continuar = True

while continuar:
    print("Bienvenido al cajero automático")
    saldo_cuenta, saldo_cajero = realizar_retiro(saldo_cuenta, saldo_cajero)
    respuesta = ("S para salir: ")
    if respuesta.upper() != "N":
       continuar = False

