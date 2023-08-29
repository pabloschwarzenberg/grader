#Cajero Automático
saldo_cuenta = 100000
saldo_cajero = 1000000
intentos_fallidos = 0

while True:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario == "10334151" and clave == "1803":
        while True:
            monto_retiro = int(input("Ingrese el monto a retirar: "))

            if monto_retiro <= 0:
                print("Monto no permitido.")
            elif monto_retiro > saldo_cuenta:
                print("Monto no permitido. Saldo insuficiente en la cuenta.")
            elif monto_retiro > saldo_cajero:
                print("Monto no permitido. Saldo insuficiente en el cajero.")
            else:
                saldo_cuenta -= monto_retiro
                saldo_cajero -= monto_retiro
                print("Retiro exitoso.")
                print("Saldo cuenta =", saldo_cuenta)
                print("Saldo cajero =", saldo_cajero)
                break
    else:
        intentos_fallidos += 1
        print("Clave inválida.")

        if intentos_fallidos == 3:
            print("Tarjeta bloqueada.")
            break

    continuar = input("¿Desea realizar otra transacción? (S/N): ")
    if continuar.upper() != "S":
        break

