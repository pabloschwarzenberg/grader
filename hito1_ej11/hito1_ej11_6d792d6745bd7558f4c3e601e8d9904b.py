#Cajero Automático
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
        print("Acceso permitido")
        break
    else:
        intentos_fallidos += 1
        print("Clave inválida")
        if intentos_fallidos == 3:
            print("Tarjeta bloqueada")
            exit()

while True:
    monto_retiro = float(input("Ingrese el monto a retirar: "))

    if monto_retiro <= 0 or monto_retiro > saldo_cuenta:
        print("Monto no permitido")
    else:
        if monto_retiro <= billetes_20000 * 20000 + billetes_10000 * 10000 + billetes_5000 * 5000:
            billetes_entregados = {
                "billetes_20000": 0,
                "billetes_10000": 0,
                "billetes_5000": 0
            }

            while monto_retiro >= 20000 and billetes_20000 > 0:
                monto_retiro -= 20000
                billetes_20000 -= 1
                billetes_entregados["billetes_20000"] += 1

            while monto_retiro >= 10000 and billetes_10000 > 0:
                monto_retiro -= 10000
                billetes_10000 -= 1
                billetes_entregados["billetes_10000"] += 1

            while monto_retiro >= 5000 and billetes_5000 > 0:
                monto_retiro -= 5000
                billetes_5000 -= 1
                billetes_entregados["billetes_5000"] += 1

            saldo_cuenta -= monto_retiro
            saldo_cajero -= monto_retiro

            print(f"Saldo cuenta: {saldo_cuenta}")
            print(f"Saldo cajero: {saldo_cajero}")
            print("Billetes entregados:")
            for billete, cantidad in billetes_entregados.items():
                if cantidad > 0:
                    print(f"{billete} = {cantidad}")

        else:
            print("Monto no permitido")

    continuar = input("¿Desea realizar otra transacción? (N para salir): ")
    if continuar.upper() != "N":
        break

