#Cajero Automático
saldo_inicial = 1000000
saldo_cuenta = 100000
saldo_cajero = saldo_inicial
billetes_20000 = 20
billetes_10000 = 40
billetes_5000 = 40

intentos = 0
bloqueado = False

while True:
    usuario = float(input("Ingrese su usuario: "))
    clave = float(input("Ingrese su clave: "))

    if usuario == "10334151" and clave == "1803":
        intentos = 0
        bloqueado = False
        while True:
            if bloqueado:
                print("Tarjeta bloqueada. Programa finalizado.")
                break

            monto = float(input("Ingrese el monto a retirar: "))

            if monto <= 0:
                print("Monto no permitido.")
            elif monto > saldo_cuenta:
                print("Saldo insuficiente.")
            elif monto > saldo_cajero:
                print("No hay suficiente dinero en el cajero.")
            else:
                # Distribución de billetes
                billetes_20000_retiro = min(int(monto / 20000), billetes_20000)
                monto -= billetes_20000_retiro * 20000
                billetes_10000_retiro = min(int(monto / 10000), billetes_10000)
                monto -= billetes_10000_retiro * 10000
                billetes_5000_retiro = min(int(monto / 5000), billetes_5000)
                monto -= billetes_5000_retiro * 5000

                saldo_cuenta -= (billetes_20000_retiro * 20000 +
                                 billetes_10000_retiro * 10000 +
                                 billetes_5000_retiro * 5000)
                saldo_cajero -= (billetes_20000_retiro * 20000 +
                                 billetes_10000_retiro * 10000 +
                                 billetes_5000_retiro * 5000)
                billetes_20000 -= billetes_20000_retiro
                billetes_10000 -= billetes_10000_retiro
                billetes_5000 -= billetes_5000_retiro

                print("Retiro exitoso.")
                print("Saldo cuenta =", saldo_cuenta)
                print("Saldo cajero =", saldo_cajero)
                print("Billetes de 20000 =", billetes_20000_retiro)
                print("Billetes de 10000 =", billetes_10000_retiro)
                print("Billetes de 5000 =", billetes_5000_retiro)

            respuesta = input("¿Desea realizar otro retiro? (S/N): ")
            if respuesta.upper() != "S":
                print("Programa finalizado.")
                break
    else:
        intentos += 1
        print("Clave inválida.")
        if intentos == 3:
            bloqueado = True
            print("Tarjeta bloqueada. Programa finalizado.")
            break
      