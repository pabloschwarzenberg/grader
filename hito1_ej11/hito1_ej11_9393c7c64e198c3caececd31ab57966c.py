#Cajero Automático
saldo_inicial = 1000000
saldo_usuario = 100000
billetes_disponibles = {20000: 20, 10000: 40, 5000: 40}
intentos_fallidos = 0
usuario = input("Ingrese el usuario: ")
clave = input("Ingrese la clave: ")

if usuario == "10334151" and clave == "1803":
    while True:
        monto = float(input("Ingrese el monto a retirar: "))

        if monto <= 0:
            print("Monto no permitido.")
        elif monto > saldo_inicial:
            print("Saldo insuficiente.")
        else:
            billetes_entregados = {}
            saldo_inicial -= monto
            saldo_usuario -= monto
            for denominacion, cantidad_disponible in billetes_disponibles.items():
                cantidad_billetes = min(int(monto / denominacion), cantidad_disponible)
                billetes_entregados[denominacion] = cantidad_billetes
                monto -= denominacion * cantidad_billetes
                if monto == 0:
                    break

            print("Saldo cuenta={}".format(int(saldo_usuario)))
            print("Saldo cajero={}".format(int(saldo_inicial)))
            print(str(denominacion * cantidad_billetes))

            for denominacion, cantidad in billetes_entregados.items():
                print("Billetes", denominacion, "=", cantidad)

        continuar = input("¿Desea hacer otro retiro? (S/N): ")
        if continuar != "S":
            break

    intentos_fallidos = 0  # Reiniciar el contador de intentos fallidos
else:
    print("Clave inválida.")
    intentos_fallidos += 1

if intentos_fallidos >= 3:
    print("Tarjeta bloqueada.")