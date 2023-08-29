saldo_inicial = 1000000
saldo_cajero = saldo_inicial
usuario_valido = 10334151
clave_valida = 1803
intentos_fallidos = 0

billetes_20000 = 20
billetes_10000 = 40
billetes_5000 = 40

while True:
    usuario = int(input("Ingrese su número de usuario: "))
    clave = int(input("Ingrese su clave: "))

    if usuario == usuario_valido and clave == clave_valida:
        saldo_usuario = 100000
        print("Bienvenido al cajero automático.")
        break
    else:
        intentos_fallidos += 1
        if intentos_fallidos == 3:
            print("Tarjeta bloqueada.")
            exit()
        else:
            print("Clave inválida. Por favor, inténtelo nuevamente.")

while True:
    monto_retiro = int(input("Ingrese el monto a retirar: "))

    if monto_retiro <= 0:
        print("Monto no permitido.")
    elif monto_retiro > saldo_usuario or monto_retiro > saldo_cajero:
        print("Saldo insuficiente.")
    else:
        billetes_20000_retiro = min(monto_retiro // 20000, billetes_20000)
        monto_retiro -= billetes_20000_retiro * 20000
        billetes_10000_retiro = min(monto_retiro // 10000, billetes_10000)
        monto_retiro -= billetes_10000_retiro * 10000
        billetes_5000_retiro = min(monto_retiro // 5000, billetes_5000)
        monto_retiro -= billetes_5000_retiro * 5000

        if monto_retiro > 0:
            print("No es posible retirar el monto solicitado.")
        else:
            saldo_usuario -= (billetes_20000_retiro * 20000) + (billetes_10000_retiro * 10000) + (billetes_5000_retiro * 5000)
            saldo_cajero -= (billetes_20000_retiro * 20000) + (billetes_10000_retiro * 10000) + (billetes_5000_retiro * 5000)

            print("Retiro exitoso.")
            print("Saldo cuenta =", saldo_usuario)
            print("Saldo cajero =", saldo_cajero)
            print("Billetes 20000 =", billetes_20000_retiro)
            print("Billetes 10000 =", billetes_10000_retiro)
            print("Billetes 5000 =", billetes_5000_retiro)

            billetes_20000 -= billetes_20000_retiro
            billetes_10000 -= billetes_10000_retiro
            billetes_5000 -= billetes_5000_retiro

    continuar = input("¿Desea realizar otra transacción? (S/N): ")
    if continuar.upper() != "S":
        break
