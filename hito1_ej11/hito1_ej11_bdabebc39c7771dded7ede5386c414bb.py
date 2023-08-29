#Cajero Automático
saldo_inicial = 1000000
saldo_cuenta = 100000
saldo_cajero = saldo_inicial

billetes_20000 = 20
billetes_10000 = 40
billetes_5000 = 40

intentos = 0
usuario_valido = False

while not usuario_valido:
    usuario = input("Ingrese el número de usuario: ")
    clave = input("Ingrese la clave: ")

    if usuario == "10334151" and clave == "1803":
        usuario_valido = True
    else:
        intentos += 1
        if intentos == 3:
            print("Tarjeta bloqueada.")
            exit()
        else:
            print("Clave inválida. Intente nuevamente.")

while True:
    monto = float(input("Ingrese el monto a retirar: "))

    if monto <= 0:
        print("Monto no permitido. Intente nuevamente.")
    elif monto > saldo_cuenta:
        print("Saldo insuficiente.")
    else:
        # Verificar disponibilidad de billetes
        if monto > (billetes_20000 * 20000 + billetes_10000 * 10000 + billetes_5000 * 5000):
            print("No hay suficientes billetes para el monto solicitado.")
        elif monto % 5000 != 0:
            print("El monto no se puede retirar con los billetes disponibles.")
        else:
            # Calcular cantidad de billetes necesarios
            billetes_20000_retirados = min(billetes_20000, int(monto // 20000))
            monto -= billetes_20000_retirados * 20000

            billetes_10000_retirados = min(billetes_10000, int(monto // 10000))
            monto -= billetes_10000_retirados * 10000

            billetes_5000_retirados = min(billetes_5000, int(monto // 5000))
            monto -= billetes_5000_retirados * 5000

            # Actualizar saldos
            saldo_cuenta -= (billetes_20000_retirados * 20000
                             + billetes_10000_retirados * 10000
                             + billetes_5000_retirados * 5000)
            saldo_cajero -= (billetes_20000_retirados * 20000
                             + billetes_10000_retirados * 10000
                             + billetes_5000_retirados * 5000)
            billetes_20000 -= billetes_20000_retirados
            billetes_10000 -= billetes_10000_retirados
            billetes_5000 -= billetes_5000_retirados

            # Imprimir resultado
            print("Retiro exitoso.")
            print("Saldo cuenta =", saldo_cuenta)
            print("Saldo cajero =", saldo_cajero)
            print("Billetes 20000 =", billetes_20000_retirados)
            print("Billetes 10000 =", billetes_10000_retirados)
            print
