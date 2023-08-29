saldo_cuenta = 100000
saldo_cajero = 1000000
billetes_20000 = 20
billetes_10000 = 40
billetes_5000 = 40

intentos_fallidos = 0

while True:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario == "10334151" and clave == "1803":
        print("Bienvenido/a")
        break
    else:
        intentos_fallidos += 1
        print("Clave inválida")

    if intentos_fallidos == 3:
        print("Tarjeta bloqueada")
        exit()

while True:
    monto_retiro = float(input("Ingrese el monto a retirar: "))

    if monto_retiro > saldo_cuenta or monto_retiro <= 0:
        print("Monto no permitido")
    else:
        billetes_20000_retiro = min(billetes_20000, int(monto_retiro / 20000))
        monto_retiro -= billetes_20000_retiro * 20000

        billetes_10000_retiro = min(billetes_10000, int(monto_retiro / 10000))
        monto_retiro -= billetes_10000_retiro * 10000

        billetes_5000_retiro = min(billetes_5000, int(monto_retiro / 5000))
        monto_retiro -= billetes_5000_retiro * 5000

        saldo_cuenta -= (billetes_20000_retiro * 20000) + (billetes_10000_retiro * 10000) + (billetes_5000_retiro * 5000)
        saldo_cajero -= (billetes_20000_retiro * 20000) + (billetes_10000_retiro * 10000) + (billetes_5000_retiro * 5000)

        print("Retiro exitoso. Su saldo actual es: Saldo cuenta =", saldo_cuenta, "Saldo cajero =", saldo_cajero)
        print("30000 ")
        print("billetes 20000 =", billetes_20000_retiro)
        print("billetes 10000 =", billetes_10000_retiro)
        print("billetes 5000 =", billetes_5000_retiro)

    continuar = input("¿Desea realizar otro retiro? (S/N): ")
    if continuar.upper() != "S":
        break