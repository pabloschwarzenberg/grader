saldo_cuenta = 100000
saldo_cajero = 1000000
intentos_fallidos = 0
billetes_20000 = 20
billetes_10000 = 40
billetes_5000 = 40

while True:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario == "10334151" and clave == "1803":
        print("Bienvenido al cajero")
        break
    else:
        print("Usuario o clave incorrectos")
        intentos_fallidos += 1

    if intentos_fallidos == 3:
        print("Tarjeta bloqueada")
        exit()

while True:
    monto_retiro = int(input("Ingrese el monto a retirar: "))

    if monto_retiro <= 0 or monto_retiro > saldo_cuenta:
        print("Monto no permitido")
    else:
        # Calcular cantidad de billetes necesarios para cada denominación
        billetes_20000_retirados = min(billetes_20000, monto_retiro // 20000)
        monto_retiro -= billetes_20000_retirados * 20000

        billetes_10000_retirados = min(billetes_10000, monto_retiro // 10000)
        monto_retiro -= billetes_10000_retirados * 10000

        billetes_5000_retirados = min(billetes_5000, monto_retiro // 5000)
        monto_retiro -= billetes_5000_retirados * 5000

        # Actualizar saldos y cantidad de billetes disponibles
        saldo_cuenta -= (billetes_20000_retirados * 20000 + billetes_10000_retirados * 10000 + billetes_5000_retirados * 5000)
        saldo_cajero -= (billetes_20000_retirados * 20000 + billetes_10000_retirados * 10000 + billetes_5000_retirados * 5000)
        billetes_20000 -= billetes_20000_retirados
        billetes_10000 -= billetes_10000_retirados
        billetes_5000 -= billetes_5000_retirados

        print("Retiro exitoso")
        print("Saldo cuenta = {}".format(saldo_cuenta))
        print("Saldo cajero = {}".format(saldo_cajero))
        print("Billetes 20000 = {}".format(billetes_20000_retirados))
        print("Billetes 10000 = {}".format(billetes_10000_retirados))
        print("Billetes 5000 = {}".format(billetes_5000_retirados))

    continuar = input("¿Desea realizar otro retiro? (S/N): ")
    if continuar != "S":
        break