saldo_cuenta = 100000
saldo_cajero = 1000000
intentos = 0
usuario_valido = 10334151
clave_valida = 1803

billetes_20000 = 20
billetes_10000 = 40
billetes_5000 = 40

while intentos < 3:
    usuario = input("Ingrese su número de usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario == str(usuario_valido) and clave == str(clave_valida):
        while True:
            try:
                monto_retiro = float(input("Ingrese el monto a retirar: "))

                if monto_retiro <= saldo_cuenta and monto_retiro <= saldo_cajero:
                    if monto_retiro % 5000 != 0:
                        print("Monto no permitido. El monto debe ser múltiplo de 5000.")
                        continue

                    # Cálculo de la distribución de billetes
                    billetes_20000_retirados = min(billetes_20000, int(monto_retiro / 20000))
                    monto_retiro -= billetes_20000_retirados * 20000
                    billetes_10000_retirados = min(billetes_10000, int(monto_retiro / 10000))
                    monto_retiro -= billetes_10000_retirados * 10000
                    billetes_5000_retirados = min(billetes_5000, int(monto_retiro / 5000))

                    saldo_cuenta -= (billetes_20000_retirados * 20000 +
                                     billetes_10000_retirados * 10000 +
                                     billetes_5000_retirados * 5000)
                    saldo_cajero -= (billetes_20000_retirados * 20000 +
                                     billetes_10000_retirados * 10000 +
                                     billetes_5000_retirados * 5000)

                    print("Retiro exitoso.")
                    print("Saldo cuenta =", saldo_cuenta)
                    print("Saldo cajero =", saldo_cajero)
                    print("Billetes 20000 =", billetes_20000_retirados)
                    print("Billetes 10000 =", billetes_10000_retirados)
                    print("Billetes 5000 =", billetes_5000_retirados)
                    break
                elif monto_retiro > saldo_cuenta:
                    print("Monto no permitido. Saldo insuficiente en la cuenta.")
                elif monto_retiro > saldo_cajero:
                    print("Monto no permitido. Saldo insuficiente en el cajero.")
            except ValueError:
                print("Error: Ingrese un monto válido.")
        break
    else:
        intentos += 1
        print("Clave inválida.")

    if intentos == 3:
        print("Tarjeta bloqueada.")
