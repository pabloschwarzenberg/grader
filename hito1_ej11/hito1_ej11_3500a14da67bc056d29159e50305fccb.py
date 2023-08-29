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
        while True:
            monto_retiro = int(input("Ingrese el monto a retirar: "))

            if monto_retiro <= 0:
                print("Monto no permitido.")
            elif monto_retiro > saldo_cuenta:
                print("Monto no permitido. Saldo insuficiente en la cuenta.")
            elif monto_retiro > saldo_cajero:
                print("Monto no permitido. Saldo insuficiente en el cajero.")
            else:
                billetes_20000_retiro = min(billetes_20000, monto_retiro // 20000)
                billetes_10000_retiro = min(billetes_10000, (monto_retiro - (billetes_20000_retiro * 20000)) // 10000)
                billetes_5000_retiro = min(billetes_5000, (monto_retiro - (billetes_20000_retiro * 20000) - (billetes_10000_retiro * 10000)) // 5000)

                if (billetes_20000_retiro * 20000) + (billetes_10000_retiro * 10000) + (billetes_5000_retiro * 5000) != monto_retiro:
                    print("Monto no permitido. No se pueden entregar los billetes exactos.")
                else:
                    saldo_cuenta -= monto_retiro
                    saldo_cajero -= monto_retiro
                    billetes_20000 -= billetes_20000_retiro
                    billetes_10000 -= billetes_10000_retiro
                    billetes_5000 -= billetes_5000_retiro

                    print("Retiro exitoso.")
                    print("Saldo cuenta =", saldo_cuenta)
                    print("Saldo cajero =", saldo_cajero)
                    print("Billetes 20000 =", billetes_20000_retiro)
                    print("Billetes 10000 =", billetes_10000_retiro)
                    print("Billetes 5000 =", billetes_5000_retiro)
                    break
    else:
        intentos_fallidos += 1
        print("Clave inválida.")

        if intentos_fallidos == 3:
            print("Tarjeta bloqueada.")
            break

    continuar = input("¿Desea realizar otra transacción? (S/N): ")
    if continuar.upper() != "S":
        break