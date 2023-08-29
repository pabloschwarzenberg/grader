def cajero():
    # Datos de usuario y clave
    usuario_valido = 10334151
    clave_valida = 1803
    intentos = 0

    # Saldo inicial y cantidad de billetes
    saldo_cuenta = 100000
    saldo_cajero = 1000000
    billetes_20000 = 20
    billetes_10000 = 40
    billetes_5000 = 40

    # Validación de usuario y clave
    while True:
        usuario = int(input("Ingrese su número de usuario: "))
        clave = int(input("Ingrese su clave: "))

        if usuario == usuario_valido and clave == clave_valida:
            print("Acceso permitido")
            break
        else:
            intentos += 1
            print("Clave inválida")

        if intentos == 3:
            print("Tarjeta bloqueada")
            return

    # Retiro de dinero
    monto = float(input("Ingrese el monto a retirar: "))

    if monto > saldo_cuenta:
        print("Monto no permitido")
    else:
        # Cálculo de billetes a entregar
        billetes_entregados_20000 = min(billetes_20000, int(monto / 20000))
        monto -= billetes_entregados_20000 * 20000

        billetes_entregados_10000 = min(billetes_10000, int(monto / 10000))
        monto -= billetes_entregados_10000 * 10000

        billetes_entregados_5000 = min(billetes_5000, int(monto / 5000))
        monto -= billetes_entregados_5000 * 5000

        # Actualización de saldos y cantidad de billetes
        saldo_cuenta -= (billetes_entregados_20000 * 20000
                         + billetes_entregados_10000 * 10000
                         + billetes_entregados_5000 * 5000)

        saldo_cajero -= (billetes_entregados_20000 * 20000
                         + billetes_entregados_10000 * 10000
                         + billetes_entregados_5000 * 5000)

        billetes_20000 -= billetes_entregados_20000
        billetes_10000 -= billetes_entregados_10000
        billetes_5000 -= billetes_entregados_5000

        print("Retiro exitoso")
        print(f"Saldo cuenta: {saldo_cuenta}")
        print(f"Saldo cajero: {saldo_cajero}")
        print("Billetes entregados:")
        print(f"Billetes 20000: {billetes_entregados_20000}")
        print(f"Billetes 10000: {billetes_entregados_10000}")
        print(f"Billetes 5000: {billetes_entregados_5000}")


# Ejecutar el programa del cajero
cajero()
