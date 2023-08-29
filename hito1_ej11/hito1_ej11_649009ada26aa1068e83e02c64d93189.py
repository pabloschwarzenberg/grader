billetes_20000 = 20
billetes_10000 = 40
billetes_5000 = 40

saldo_cuenta = billetes_20000 * 20000 + billetes_10000 * 10000 + billetes_5000 * 5000
saldo_cajero = saldo_cuenta

intentos_fallidos = 0

while True:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario == "10334151" and clave == "1803":
        print(f"Bienvenido(a) al cajero.")
        break
    else:
        print("Clave inválida.")
        intentos_fallidos += 1

    if intentos_fallidos == 3:
        print("Tarjeta bloqueada.")
        exit()

while True:
    monto_retiro = float(input("Ingrese el monto a retirar: "))

    if monto_retiro <= 0:
        print("Monto no permitido.")
    elif monto_retiro > saldo_cuenta:
        print("Saldo insuficiente.")
    else:
        billetes_entregados = {
            20000: 0,
            10000: 0,
            5000: 0
        }

        # Distribuir el monto en billetes de la denominación más alta posible
        while monto_retiro >= 20000 and billetes_20000 > 0:
            billetes_entregados[20000] += 1
            billetes_20000 -= 1
            monto_retiro -= 20000

        while monto_retiro >= 10000 and billetes_10000 > 0:
            billetes_entregados[10000] += 1
            billetes_10000 -= 1
            monto_retiro -= 10000

        while monto_retiro >= 5000 and billetes_5000 > 0:
            billetes_entregados[5000] += 1
            billetes_5000 -= 1
            monto_retiro -= 5000

        if monto_retiro == 0:
            saldo_cuenta -= (billetes_entregados[20000] * 20000 +
                             billetes_entregados[10000] * 10000 +
                             billetes_entregados[5000] * 5000)
            saldo_cajero = saldo_cuenta

            print("Retiro exitoso.")
            print("Saldo cuenta =", saldo_cuenta)
            print("Saldo cajero =", saldo_cajero)
            print("Billetes entregados:")
            for denominacion, cantidad in billetes_entregados.items():
                if cantidad > 0:
                    print("{denominacion}: {cantidad}")
        else:
            print("No es posible entregar el monto solicitado con los billetes disponibles.")

    opcion = input("¿Desea realizar otro retiro? (S/N): ")
    if opcion.upper() != "S":
        break
