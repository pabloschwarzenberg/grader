def cajero():
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
            break
        else:
            intentos_fallidos += 1
            print("Clave inválida.")

        if intentos_fallidos == 3:
            print("Tarjeta bloqueada. Intente más tarde.")
            exit()

    while True:
        monto_retiro = float(input("Ingrese el monto a retirar: "))
        total_billetes = monto_retiro

        if monto_retiro > saldo_cuenta:
            print("Monto no permitido. Saldo insuficiente en la cuenta.")
        elif monto_retiro > saldo_cajero:
            print("Monto no permitido. Saldo insuficiente en el cajero.")
        else:
            saldo_cuenta -= monto_retiro
            saldo_cajero -= monto_retiro
            
            # Distribución de billetes
            billetes_20000_retiro = min(billetes_20000, monto_retiro // 20000)
            total_billetes -= billetes_20000_retiro * 20000

            billetes_10000_retiro = min(billetes_10000, total_billetes // 10000)
            total_billetes -= billetes_10000_retiro * 10000

            billetes_5000_retiro = min(billetes_5000, total_billetes // 5000)
            total_billetes -= billetes_5000_retiro * 5000

            saldo_cuenta -= (billetes_20000_retiro * 20000) + (billetes_10000_retiro * 10000) + (billetes_5000_retiro * 5000)
            saldo_cajero -= (billetes_20000_retiro * 20000) + (billetes_10000_retiro * 10000) + (billetes_5000_retiro * 5000)


            print("['saldo cuenta="+str(int(saldo_cuenta))+"','saldo cajero="+str(int(saldo_cajero))+"']['billetes 20000="+str(int(billetes_20000_retiro))+"', 'billetes 10000="+str(int(billetes_10000_retiro))+"','billetes 5000="+str(int(billetes_5000_retiro))+"']")

        opcion = input("¿Desea realizar otro retiro? (S/N): ")
        if opcion.upper() == "N":
            break
