saldo_cajero = 1000000
saldo_usuario = 100000

intentos_fallidos = 0

billetes_20000 = 20
billetes_10000 = 40
billetes_5000 = 40

while True:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario == "10334151" and clave == "1803":
        intentos_fallidos = 0

        monto = int(input("Ingrese el monto a retirar: "))

        if monto > saldo_usuario or monto > saldo_cajero:
            print("Monto no permitido")
        else:
            saldo_usuario -= monto
            saldo_cajero -= monto

            num_billetes_20000 = monto // 20000
            monto -= num_billetes_20000 * 20000

            num_billetes_10000 = monto // 10000
            monto -= num_billetes_10000 * 10000

            num_billetes_5000 = monto // 5000

            billetes_20000 -= num_billetes_20000
            billetes_10000 -= num_billetes_10000
            billetes_5000 -= num_billetes_5000

            print("saldo cuenta=" + str(saldo_usuario))
            print("saldo cajero=" + str(saldo_cajero))
            print("billetes 20000=" + str(num_billetes_20000))
            print("billetes 10000=" + str(num_billetes_10000))
            print("billetes 5000=" + str(num_billetes_5000))
    else:
        intentos_fallidos += 1

        if intentos_fallidos == 3:
            print("Tarjeta bloqueada")
            break
        else:
            print("Clave invalida")

    continuar = input("¿Desea continuar? (N para salir): ")
    if continuar != "N":
        break
  