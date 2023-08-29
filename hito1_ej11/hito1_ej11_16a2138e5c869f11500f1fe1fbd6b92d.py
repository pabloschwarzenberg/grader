#Cajero Automático
saldo_inicial = 1000000
saldo_cuenta = 100000
saldo_cajero = saldo_inicial - saldo_cuenta
billetes_20000 = 20
billetes_10000 = 40
billetes_5000 = 40
intentos_fallidos = 0

while True:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario == "10334151" and clave == "1803":
        print("Bienvenido")
        break
    else:
        intentos_fallidos += 1
        print("Clave inválida")

        if intentos_fallidos == 3:
            print("Tarjeta bloqueada")
            exit()

while True:
    monto_retiro = float(input("Ingrese el monto a retirar: "))

    if monto_retiro <= saldo_cuenta:
        if monto_retiro > saldo_cajero:
            print("Monto no permitido")
        else:
            # Cálculo de la distribución de billetes
            billetes_20000_retirados = min(billetes_20000, int(monto_retiro / 20000))
            monto_retiro -= billetes_20000_retirados * 20000
            billetes_10000_retirados = min(billetes_10000, int(monto_retiro / 10000))
            monto_retiro -= billetes_10000_retirados * 10000
            billetes_5000_retirados = min(billetes_5000, int(monto_retiro / 5000))
            monto_retiro -= billetes_5000_retirados * 5000

            saldo_cuenta -= (billetes_20000_retirados * 20000 +
                             billetes_10000_retirados * 10000 +
                             billetes_5000_retirados * 5000)
            saldo_cajero -= (billetes_20000_retirados * 20000 +
                             billetes_10000_retirados * 10000 +
                             billetes_5000_retirados * 5000)
            billetes_20000 -= billetes_20000_retirados
            billetes_10000 -= billetes_10000_retirados
            billetes_5000 -= billetes_5000_retirados

            print("saldo cuenta =", saldo_cuenta)
            print("saldo cajero =", saldo_cajero)
            print("billetes 20000 =", billetes_20000_retirados)
            print("billetes 10000 =", billetes_10000_retirados)
            print("billetes 5000 =", billetes_5000_retirados)
    else:
        print("Monto no permitido")

    opcion = input("¿Desea hacer otro retiro? (S/N): ")

    if opcion.upper() != "S":
        break
