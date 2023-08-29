#Cajero Automático
#Cajero Automático
saldo_cuenta = 100000
saldo_cajero = 1000000
billetes_20000 = 20
billetes_10000 = 40
billetes_5000 = 40
intentos = 0

usuario_valido = 10334151
clave_valida = 1803

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
    monto = float(input("Ingrese el monto a retirar: "))

    if monto <= 0:
        print("Monto no permitido")
    elif monto > saldo_cuenta:
        print("Saldo insuficiente")
    else:
        billetes_20000_retirados = min(int(monto / 20000), billetes_20000)
        monto -= billetes_20000_retirados * 20000
        billetes_10000_retirados = min(int(monto / 10000), billetes_10000)
        monto -= billetes_10000_retirados * 10000
        billetes_5000_retirados = min(int(monto / 5000), billetes_5000)
        monto -= billetes_5000_retirados * 5000

        if monto > 0:
            print("No se puede retirar el monto exacto con los billetes disponibles")
        else:
            saldo_cuenta -= (billetes_20000_retirados * 20000 + billetes_10000_retirados * 10000 + billetes_5000_retirados * 5000)
            saldo_cajero -= (billetes_20000_retirados * 20000 + billetes_10000_retirados * 10000 + billetes_5000_retirados * 5000)

            print("Retiro exitoso")
            print("Saldo cuenta =", saldo_cuenta)
            print("Saldo cajero =", saldo_cajero)
            print("Billetes 20000 =", billetes_20000_retirados)
            print("Billetes 10000 =", billetes_10000_retirados)
            print("Billetes 5000 =", billetes_5000_retirados)

    opcion = input("¿Desea realizar otro retiro? (S/N): ")
    if opcion.upper() != "S":
        break
      