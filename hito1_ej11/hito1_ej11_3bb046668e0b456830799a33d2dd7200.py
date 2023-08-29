#Cajero Automático
saldo_inicial = 1000000
saldo_cuenta = 100000
saldo_cajero = saldo_inicial
usuario_valido = 10334151
clave_valida = 1803
intentos_fallidos = 0

billetes_20000 = 20
billetes_10000 = 40
billetes_5000 = 40

while True:
    usuario = int(input("Ingrese su usuario: "))
    clave = int(input("Ingrese su clave: "))
    if usuario == usuario_valido and clave == clave_valida:
        print("Inicio de sesión exitoso.")
        break
    else:
        intentos_fallidos += 1
        print("Clave inválida.")
        if intentos_fallidos == 3:
            print("Tarjeta bloqueada.")
            exit()

while True:
    monto = float(input("Ingrese el monto a retirar: "))
    if monto <= 0:
        print("Monto no permitido.")
    elif monto > saldo_cuenta:
        print("Saldo insuficiente.")
    elif monto > saldo_cajero:
        print("El cajero no dispone de suficiente efectivo.")
    else:
        # Calcula la cantidad de billetes de cada denominación a entregar
        billetes_entregados_20000 = min(monto // 20000, billetes_20000)
        monto -= billetes_entregados_20000 * 20000

        billetes_entregados_10000 = min(monto // 10000, billetes_10000)
        monto -= billetes_entregados_10000 * 10000

        billetes_entregados_5000 = min(monto // 5000, billetes_5000)
        monto -= billetes_entregados_5000 * 5000

        saldo_cuenta -= (billetes_entregados_20000 * 20000 +
                         billetes_entregados_10000 * 10000 +
                         billetes_entregados_5000 * 5000)
        saldo_cajero -= (billetes_entregados_20000 * 20000 +
                         billetes_entregados_10000 * 10000 +
                         billetes_entregados_5000 * 5000)

        print("Retiro exitoso.")
        print("Saldo cuenta: {}".format(saldo_cuenta))
        print("Saldo cajero: {}".format(saldo_cajero))

        # Imprime la cantidad de billetes entregados
        print("Billetes 20000: {}".format(billetes_entregados_20000))
        print("Billetes 10000: {}".format(billetes_entregados_10000))
        print("Billetes 5000: {}".format(billetes_entregados_5000))

    opcion = input("¿Desea realizar otro retiro? (N para salir): ")
    if opcion.upper() == "N":
        break
      