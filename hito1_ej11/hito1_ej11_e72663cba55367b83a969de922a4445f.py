billetes_20000 = 20
billetes_10000 = 40
billetes_5000 = 40

saldo_cuenta = 100000

saldo_cajero = 1000000

intentos_fallidos = 0

usuario_valido = 10334151
clave_valida = 1803

usuario = int(input("Ingrese su usuario: "))
clave = int(input("Ingrese su clave: "))

while usuario != usuario_valido or clave != clave_valida:
    intentos_fallidos += 1
    if intentos_fallidos == 3:
        print("Tarjeta bloqueada. Ha excedido el número máximo de intentos.")
        exit()
    print("Clave inválida. Por favor, ingrese nuevamente.")
    usuario = int(input("Ingrese su usuario: "))
    clave = int(input("Ingrese su clave: "))

monto_retiro = float(input("Ingrese el monto a retirar: "))

if monto_retiro <= 0 or monto_retiro > saldo_cuenta:
    print("Monto no permitido.")
else:
    billetes_20000_entregados = min(billetes_20000, int(monto_retiro / 20000))
    monto_retiro -= billetes_20000_entregados * 20000

    billetes_10000_entregados = min(billetes_10000, int(monto_retiro / 10000))
    monto_retiro -= billetes_10000_entregados * 10000

    billetes_5000_entregados = min(billetes_5000, int(monto_retiro / 5000))
    monto_retiro -= billetes_5000_entregados * 5000

    saldo_cuenta -= (billetes_20000_entregados * 20000) + (billetes_10000_entregados * 10000) + (billetes_5000_entregados * 5000)
    saldo_cajero -= (billetes_20000_entregados * 20000) + (billetes_10000_entregados * 10000) + (billetes_5000_entregados * 5000)

    print("billetes 20000=" + str(billetes_20000_entregados))
    print("billetes 10000=" + str(billetes_10000_entregados))
    print("billetes 5000=" + str(billetes_5000_entregados))

    print("saldo cuenta=" + str(saldo_cuenta))
    print("saldo cajero=" + str(saldo_cajero))