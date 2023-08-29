#Cajero Automático
saldo_inicial = 1000000
billetes_20000 = 20
billetes_10000 = 40
billetes_5000 = 40
intentos_fallidos = 0

usuario_valido = 10334151
clave_valida = 1803
saldo_usuario = 100000

while True:
    usuario = int(input("Ingrese su usuario: "))
    clave = int(input("Ingrese su clave: "))

    if usuario == usuario_valido and clave == clave_valida:
        print("Bienvenido al cajero automático")
        break
    else:
        print("Usuario o clave incorrectos")
        intentos_fallidos += 1

    if intentos_fallidos == 3:
        print("Tarjeta bloqueada")
        exit()

while True:
    try:
        monto_retiro = int(input("Ingrese el monto a retirar: "))
    except ValueError:
        print("Error: Ingrese un valor numérico válido.")
        continue

    if monto_retiro <= saldo_usuario:
        if monto_retiro <= saldo_inicial:
            if monto_retiro % 5000 == 0:
                total_billetes = billetes_20000 * 20000 + billetes_10000 * 10000 + billetes_5000 * 5000

                if monto_retiro <= total_billetes:
                    billetes_20000_retirados = min(monto_retiro // 20000, billetes_20000)
                    monto_retiro -= billetes_20000_retirados * 20000
                    billetes_10000_retirados = min(monto_retiro // 10000, billetes_10000)
                    monto_retiro -= billetes_10000_retirados * 10000
                    billetes_5000_retirados = min(monto_retiro // 5000, billetes_5000)

                    saldo_usuario -= (billetes_20000_retirados * 20000) + (billetes_10000_retirados * 10000) + (billetes_5000_retirados * 5000)
                    saldo_inicial -= (billetes_20000_retirados * 20000) + (billetes_10000_retirados * 10000) + (billetes_5000_retirados * 5000)

                    print("Retiro exitoso")
                    print("saldo cuenta=", saldo_usuario)
                    print("saldo cajero=", saldo_inicial)
                    print("billetes 20000=", billetes_20000_retirados)
                    print("billetes 10000=", billetes_10000_retirados)
                    print("billetes 5000=", billetes_5000_retirados)

                    billetes_20000 -= billetes_20000_retirados
                    billetes_10000 -= billetes_10000_retirados
                    billetes_5000 -= billetes_5000_retirados
                else:
                    print("Monto no permitido: No hay suficientes billetes disponibles en el cajero")
            else:
                print("Monto no permitido: El monto debe ser múltiplo de 5000")
        else:
            print("Monto no permitido: Fondos insuficientes en el cajero")
    else:
        print("Monto no permitido: Fondos insuficientes en la cuenta")

    opcion = input("¿Desea realizar otro retiro? (S/N): ")
    if opcion.upper() != "S":
        break
     