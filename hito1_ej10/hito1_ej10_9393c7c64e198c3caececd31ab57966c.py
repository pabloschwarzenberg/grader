#Cajero Automático
saldo_inicial = 1000000
saldo_usuario = 100000
intentos_fallidos = 0

usuario = input("Ingrese el usuario: ")
clave = input("Ingrese la clave: ")
if usuario == "10334151" and clave == "1803":
    while True:
        monto = int(input("Ingrese el monto a retirar: "))

        if monto <= 0:
            print("Monto no permitido.")
        elif monto > saldo_usuario:
            print("Saldo insuficiente.")
        else:
            saldo_usuario -= monto
            saldo_inicial -= monto
            print("Retiro exitoso.")
            print("Saldo cuenta={}".format(saldo_usuario))
            print("Saldo cajero={}".format(saldo_inicial))

        continuar = input("¿Desea hacer otro retiro? (S/N): ")
        if continuar != "S":
            break

    intentos_fallidos = 0  # Reiniciar el contador de intentos fallidos
else:
    print("Clave inválida.")
    intentos_fallidos += 1

if intentos_fallidos >= 3:
    print("Tarjeta bloqueada.")