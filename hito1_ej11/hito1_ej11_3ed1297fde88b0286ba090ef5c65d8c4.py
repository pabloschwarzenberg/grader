saldo_cuenta = 100000
saldo_cajero = 1000000
billetes_20000 = 20
billetes_10000 = 40
billetes_5000 = 40
intentos = 0

while True:
    usuario = input("Ingrese el usuario: ")
    clave = input("Ingrese la clave: ")
 
    if usuario == "10334151" and clave == "1803":
        while True:
            monto = float(input("Ingrese el monto a retirar: "))

            if monto <= 0:
                print("Monto no permitido.")
            elif monto > saldo_cuenta:
                print("Saldo insuficiente.")
            else:
                # Verificar si hay suficientes billetes para el retiro
                if monto % 5000 != 0 or monto > (billetes_20000 * 20000 + billetes_10000 * 10000 + billetes_5000 * 5000):
                    print("No se pueden entregar los billetes solicitados.")
                else:
                    # Calcular la cantidad de billetes de cada denominación
                    billetes_20000_retirados = min(billetes_20000, int(monto / 20000))
                    monto -= billetes_20000_retirados * 20000

                    billetes_10000_retirados = min(billetes_10000, int(monto / 10000))
                    monto -= billetes_10000_retirados * 10000

                    billetes_5000_retirados = min(billetes_5000, int(monto / 5000))
                    monto -= billetes_5000_retirados * 5000

                    # Actualizar los saldos y la cantidad de billetes disponibles
                    saldo_cuenta -= (billetes_20000_retirados * 20000 + billetes_10000_retirados * 10000 + billetes_5000_retirados * 5000)
                    saldo_cajero -= (billetes_20000_retirados * 20000 + billetes_10000_retirados * 10000 + billetes_5000_retirados * 5000)
                    billetes_20000 -= billetes_20000_retirados
                    billetes_10000 -= billetes_10000_retirados
                    billetes_5000 -= billetes_5000_retirados

                    print("Retiro exitoso.")
                    print("Saldo cuenta =", saldo_cuenta)
                    print("Saldo cajero =", saldo_cajero)
                    print("Billetes 20000 =", billetes_20000_retirados)
                    print("Billetes 10000 =", billetes_10000_retirados)
                    print("Billetes 5000 =", billetes_5000_retirados)

                break
    else:
        intentos += 1
        if intentos == 3:
            print("Tarjeta bloqueada.")
            break
        print("Clave inválida.")
 
    opcion = input("¿Desea realizar otra transacción? (S/N): ")
    if opcion.upper() != "S":
        break
