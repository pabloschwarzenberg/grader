#Cajero Automático
billetes_20000 = 20  # Cantidad inicial de billetes de 20.000
billetes_10000 = 40  # Cantidad inicial de billetes de 10.000
billetes_5000 = 40  # Cantidad inicial de billetes de 5.000
saldo_inicial = billetes_20000 * 20000 + billetes_10000 * 10000 + billetes_5000 * 5000
saldo_usuario = 100000
intentos = 0

while True:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario == "10334151" and clave == "1803":
        print("Acceso permitido")
        break
    else:
        print("Clave inválida")
        intentos += 1

    if intentos == 3:
        print("Tarjeta bloqueada")
        exit()

while True:
    monto = float(input("Ingrese el monto a retirar: "))

    if monto > saldo_usuario:
        print("Monto no permitido")
    else:
        # Verificar si se pueden distribuir los billetes correctamente
        if monto > saldo_inicial:
            print("El cajero no dispone del monto solicitado")
        else:
            # Calcular la cantidad de billetes de cada denominación
            billetes_20000_retirados = min(billetes_20000, int(monto / 20000))
            monto -= billetes_20000_retirados * 20000
            billetes_10000_retirados = min(billetes_10000, int(monto / 10000))
            monto -= billetes_10000_retirados * 10000
            billetes_5000_retirados = min(billetes_5000, int(monto / 5000))
            monto -= billetes_5000_retirados * 5000

            # Actualizar saldos y mostrar resultados
            saldo_usuario -= (billetes_20000_retirados * 20000 +
                              billetes_10000_retirados * 10000 +
                              billetes_5000_retirados * 5000)
            saldo_inicial -= (billetes_20000_retirados * 20000 +
                              billetes_10000_retirados * 10000 +
                              billetes_5000_retirados * 5000)

            print("Retiro exitoso")
            print("Saldo cuenta =", saldo_usuario)
            print("Saldo cajero =", saldo_inicial)
            print("Billetes 20000 =", billetes_20000_retirados)
            print("Billetes 10000 =", billetes_10000_retirados)
            print("Billetes 5000 =", billetes_5000_retirados)

            # Actualizar cantidad de billetes disponibles
            billetes_20000 -= billetes_20000_retirados
            billetes_10000 -= billetes_10000_retirados
            billetes_5000 -= billetes_5000_retirados

    opcion = input("¿Desea realizar otro retiro? (S/N): ")
    if opcion != "S" and opcion != "s":
        break
      