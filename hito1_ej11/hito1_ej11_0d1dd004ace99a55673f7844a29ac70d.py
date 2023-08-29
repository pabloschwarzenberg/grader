   #Cajero Automático
saldo_cuenta = 100000
saldo_cajero = 1000000

intentos = 0
usuario_valido = 10334151
clave_valida = 1803

billetes_20000 = 20
billetes_10000 = 40
billetes_5000 = 40

while True:
    usuario = int(input("Ingrese su usuario: "))
    clave = int(input("Ingrese su clave: "))

    if usuario == usuario_valido and clave == clave_valida:
        break

    intentos += 1
    if intentos >= 3:
        print("Tarjeta bloqueada")
        exit()

    print("Clave inválida")
    print()

while True:
    monto = int(input("Ingrese el monto a retirar: "))
    if monto <= 0:
        print("Monto no permitido")
    elif monto > saldo_cuenta:
        print("Saldo insuficiente")
    else:
        # Verificar disponibilidad de billetes
        if monto > (billetes_20000 * 20000 + billetes_10000 * 10000 + billetes_5000 * 5000):
            print("No hay suficientes billetes para realizar el retiro")
            continue

        # Calcular cantidad de billetes a entregar
        billetes_entregados_20000 = min(monto // 20000, billetes_20000)
        monto -= billetes_entregados_20000 * 20000
        billetes_entregados_10000 = min(monto // 10000, billetes_10000)
        monto -= billetes_entregados_10000 * 10000
        billetes_entregados_5000 = min(monto // 5000, billetes_5000)
        monto -= billetes_entregados_5000 * 5000

        # Actualizar saldos y billetes disponibles
        saldo_cuenta -= (billetes_entregados_20000 * 20000 + billetes_entregados_10000 * 10000 + billetes_entregados_5000 * 5000)
        saldo_cajero -= (billetes_entregados_20000 * 20000 + billetes_entregados_10000 * 10000 + billetes_entregados_5000 * 5000)
        billetes_20000 -= billetes_entregados_20000
        billetes_10000 -= billetes_entregados_10000
        billetes_5000 -= billetes_entregados_5000

        print("Retiro exitoso")
        print("Saldo cuenta =", saldo_cuenta)
        print("Saldo cajero =", saldo_cajero)
        print("Billetes 20000 =", billetes_entregados_20000)
        print("Billetes 10000 =", billetes_entregados_10000)
        print("Billetes 5000 =", billetes_entregados_5000)

    opcion = input("¿Desea otra operación? (Si/No): ")
    if opcion.upper() != "SI":
        break
