#Cajero Automático
billetes_20000 = 20
billetes_10000 = 40
billetes_5000 = 40

saldo_cajero = billetes_20000 * 20000 + billetes_10000 * 10000 + billetes_5000 * 5000
saldo_cuenta = 100000
intentos_fallidos = 0

while True:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario == "10334151" and clave == "1803":
        print("Bienvenido, usuario autorizado.")
        break
    else:
        print("Usuario o clave incorrectos.")
        intentos_fallidos += 1

    if intentos_fallidos == 3:
        print("Tarjeta bloqueada. Por favor, contacte al banco.")
        exit()

while True:
    monto_retiro = float(input("Ingrese el monto a retirar: "))

    if monto_retiro <= 0:
        print("Monto no permitido. Intente nuevamente.")
    elif monto_retiro > saldo_cuenta:
        print("Saldo insuficiente en la cuenta. Intente nuevamente.")
    elif monto_retiro > saldo_cajero:
        print("No hay suficiente dinero en el cajero. Intente nuevamente.")
    else:
        # Cálculo de la cantidad de billetes
        cant_billetes_20000 = min(billetes_20000, int(monto_retiro / 20000))
        monto_retiro -= cant_billetes_20000 * 20000

        cant_billetes_10000 = min(billetes_10000, int(monto_retiro / 10000))
        monto_retiro -= cant_billetes_10000 * 10000

        cant_billetes_5000 = min(billetes_5000, int(monto_retiro / 5000))
        monto_retiro -= cant_billetes_5000 * 5000

        # Actualización de los saldos
        saldo_cuenta -= (cant_billetes_20000 * 20000 + cant_billetes_10000 * 10000 + cant_billetes_5000 * 5000)
        saldo_cajero -= (cant_billetes_20000 * 20000 + cant_billetes_10000 * 10000 + cant_billetes_5000 * 5000)
        billetes_20000 -= cant_billetes_20000
        billetes_10000 -= cant_billetes_10000
        billetes_5000 -= cant_billetes_5000

        # Impresión de los resultados
        print("Retiro exitoso.")
        print("Saldo cuenta =", saldo_cuenta)
        print("Saldo cajero =", saldo_cajero)
        print("Billetes 20000 =", cant_billetes_20000)
        print("Billetes 10000 =", cant_billetes_10000)
        print("Billetes 5000 =", cant_billetes_5000)

    opcion = input("¿Desea realizar otro retiro? (S/N): ")
    if opcion.upper() != "S":
        break


      